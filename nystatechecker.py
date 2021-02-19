#!/usr/local/bin/python
import requests
from pprint import pp as pprint
from twilio.rest import Client
import sys
import json

SCRAPERAPIKEY = '***REMOVED***'
#ENDPOINT = "https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers"
ENDPOINT = "http://api.scraperapi.com?api_key="+ SCRAPERAPIKEY + "&url=https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers"

TOCHECK = ["Jones Beach - Field 3", "SUNY Stony Brook University Innovation and Discovery Center", "Aqueduct Racetrack - Racing Hall","Javits Center","Westchester County Center"]
AVAILABLE_CODE = "AA"
NOT_AVAILABLE_CODE = "NAC"

PUSHOVER_API_KEY = '***REMOVED***'
PUSHOVER_USER_KEY = '***REMOVED***'

NUMBERS = ['***REMOVED***']
TWILIO_ACCT_SID = "***REMOVED***"
TWILIO_AUTH_TOKEN = "***REMOVED***"


def getAppts():
    r = requests.get(ENDPOINT)
    try:
        result = r.json()
        pprint(result)
    except json.decoder.JSONDecodeError:
        result = r.text
        print(result)
        sys.exit(1)
    return result

def getApptsTest():
    return {'providerList': [{'providerName': 'Javits Center', 'address': 'New York, NY', 'availableAppointments': 'AA'}, {'providerName': 'Jones Beach - Field 3', 'address': 'Wantagh, NY', 'availableAppointments': 'NAC'}, {'providerName': 'State Fair Expo Center: NYS Fairgrounds', 'address': 'Syracuse, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Albany ', 'address': 'Albany, NY', 'availableAppointments': 'NAC'}, {'providerName': 'Westchester County Center', 'address': 'White Plains, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Stony Brook University Innovation and Discovery Center', 'address': 'Stony Brook, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Potsdam Field House', 'address': 'Potsdam, NY', 'availableAppointments': 'AA'}, {'providerName': 'Aqueduct Racetrack - Racing Hall', 'address': 'South Ozone Park, NY', 'availableAppointments': 'NAC'}, {'providerName': 'Plattsburgh International Airport -Connecticut Building', 'address': 'Plattsburgh, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Binghamton', 'address': 'Johnson City, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Polytechnic Institute - Wildcat Field House', 'address': 'Utica, NY', 'availableAppointments': 'NAC'}, {'providerName': 'University at Buffalo South Campus - Harriman Hall', 'address': 'Buffalo, NY', 'availableAppointments': 'NAC'}, {'providerName': 'Rochester Dome Arena', 'address': 'Henrietta, NY', 'availableAppointments': 'NAC'}], 'lastUpdated': '2/11/2021, 8:01:37 PM'}
def notify(locs):
    message = 'Vaccine Appts Available at:\n'
    for name in locs:
        message = message + name + '\n'
    message = message + '\nRUN!!!!!!!'
    print(message)
    pushover(message)
    sendTexts(message)

def sendTexts(message):
    client = Client(TWILIO_ACCT_SID,TWILIO_AUTH_TOKEN)
    for num in NUMBERS:
        msg = client.messages.create(
            to=num,
            from_="***REMOVED***",
            body=message
        )
        print(msg)

def pushover(message):
    #Pushover Request
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": PUSHOVER_API_KEY,
        "user": PUSHOVER_USER_KEY,
        "title" : "VACCINE!!!",
        "message": message,
        "priority" : 1
    })
    print(r.text)

def sendText(msg):
    pass

def main():
    #Pull Appts
    appts = getAppts()
    #pprint(appts)
    availableLocs = []
    for loc in appts['providerList']:
        if loc['providerName'] in TOCHECK:
            pprint(loc)
            if loc['availableAppointments'] == "AA":
                availableLocs.append(loc['providerName'])
    if(len(availableLocs) > 0):
        notify(availableLocs)

main()