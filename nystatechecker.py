#!/usr/local/bin/python
import requests
from pprint import pp as pprint

SCRAPERAPIKEY = '8511b5e08855c3ad134c3f8c5a06557e'
#ENDPOINT = "https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers"
ENDPOINT = "http://api.scraperapi.com?api_key="+ SCRAPERAPIKEY + "&url=https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers"

TOCHECK = ["Jones Beach - Field 3", "SUNY Stony Brook University Innovation and Discovery Center", "Aqueduct Racetrack - Racing Hall","Javits Center","Westchester County Center"]
AVAILABLE_CODE = "AA"
NOT_AVAILABLE_CODE = "NAC"

PUSHOVER_API_KEY = '***REMOVED***'
PUSHOVER_USER_KEY = '***REMOVED***'

def getAppts():
    r = requests.get(ENDPOINT)
    return r.json()
def getApptsTest():
    return {'providerList': [{'providerName': 'Javits Center', 'address': 'New York, NY', 'availableAppointments': 'AA'}, {'providerName': 'Jones Beach - Field 3', 'address': 'Wantagh, NY', 'availableAppointments': 'NAC'}, {'providerName': 'State Fair Expo Center: NYS Fairgrounds', 'address': 'Syracuse, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Albany ', 'address': 'Albany, NY', 'availableAppointments': 'NAC'}, {'providerName': 'Westchester County Center', 'address': 'White Plains, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Stony Brook University Innovation and Discovery Center', 'address': 'Stony Brook, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Potsdam Field House', 'address': 'Potsdam, NY', 'availableAppointments': 'AA'}, {'providerName': 'Aqueduct Racetrack - Racing Hall', 'address': 'South Ozone Park, NY', 'availableAppointments': 'NAC'}, {'providerName': 'Plattsburgh International Airport -Connecticut Building', 'address': 'Plattsburgh, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Binghamton', 'address': 'Johnson City, NY', 'availableAppointments': 'NAC'}, {'providerName': 'SUNY Polytechnic Institute - Wildcat Field House', 'address': 'Utica, NY', 'availableAppointments': 'NAC'}, {'providerName': 'University at Buffalo South Campus - Harriman Hall', 'address': 'Buffalo, NY', 'availableAppointments': 'NAC'}, {'providerName': 'Rochester Dome Arena', 'address': 'Henrietta, NY', 'availableAppointments': 'NAC'}], 'lastUpdated': '2/11/2021, 8:01:37 PM'}
def notify(name):
    message = 'Appointments Available at ' + name + ' RUN!!!!'
    print(message)
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
    for loc in appts['providerList']:
        if loc['providerName'] in TOCHECK:
            pprint(loc)
            if loc['availableAppointments'] == "AA":
                notify(loc['providerName'])

main()