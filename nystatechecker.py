#!/usr/local/bin/python
import requests
from pprint import pp as pprint
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import sys
import json,yaml

CONFIG_FILE = 'config.yaml'
LOCATIONS_FILE = 'locations.yaml'


ENDPOINT = "https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers"

AVAILABLE_CODE = "Y"
NOT_AVAILABLE_CODE = "N"




#Returns JSON of Locations with Availability
def getAppts():
    scraperURL = "http://api.scraperapi.com?api_key="+ config['scraperapi']['api_key'] + "&url=" + ENDPOINT;
    r = requests.get(scraperURL)
    #retry once
    if r.status_code == 500:
        if(DEBUG):
            print(r.text)
        print("scraperapi request failed, trying again.")
        r = requests.get(ENDPOINT)
    try:
        result = r.json()
        if(DEBUG):
            pprint(result)
    except json.decoder.JSONDecodeError:
        result = r.text
        print("Error Reaching Endpoint. Run with \"debug:true\" for more details")
        if(DEBUG):
            print(result)
        sys.exit(1)
    return result

#Test data for getAppts
def getApptsTest():
    return {'providerList': [{'providerName': 'Javits Center', 'address': 'New York, NY', 'availableAppointments': 'Y'}, {'providerName': 'Jones Beach - Field 3', 'address': 'Wantagh, NY', 'availableAppointments': 'N'}, {'providerName': 'State Fair Expo Center: NYS Fairgrounds', 'address': 'Syracuse, NY', 'availableAppointments': 'N'}, {'providerName': 'SUNY Albany ', 'address': 'Albany, NY', 'availableAppointments': 'N'}, {'providerName': 'Westchester County Center', 'address': 'White Plains, NY', 'availableAppointments': 'N'}, {'providerName': 'SUNY Stony Brook University Innovation and Discovery Center', 'address': 'Stony Brook, NY', 'availableAppointments': 'N'}, {'providerName': 'SUNY Potsdam Field House', 'address': 'Potsdam, NY', 'availableAppointments': 'AA'}, {'providerName': 'Aqueduct Racetrack - Racing Hall', 'address': 'South Ozone Park, NY', 'availableAppointments': 'N'}, {'providerName': 'Plattsburgh International Airport -Connecticut Building', 'address': 'Plattsburgh, NY', 'availableAppointments': 'N'}, {'providerName': 'SUNY Binghamton', 'address': 'Johnson City, NY', 'availableAppointments': 'N'}, {'providerName': 'SUNY Polytechnic Institute - Wildcat Field House', 'address': 'Utica, NY', 'availableAppointments': 'N'}, {'providerName': 'University at Buffalo South Campus - Harriman Hall', 'address': 'Buffalo, NY', 'availableAppointments': 'N'}, {'providerName': 'Rochester Dome Arena', 'address': 'Henrietta, NY', 'availableAppointments': 'N'}], 'lastUpdated': '2/11/2021, 8:01:37 PM'}


#Takes dict of loctions to check and dict of availablity (appointments) from endpoint and returns arr of places with available appointment that have been preselected to look at 
def availableLocations(locations_to_check, appointments):
    availableLocs = []
    for loc in appointments['providerList']:
        if loc['providerName'] in locations_to_check and locations_to_check[loc['providerName']]:
            if loc['availableAppointments'] == AVAILABLE_CODE:
                availableLocs.append(loc['providerName'])
    return availableLocs

#Takes list of locations where vaccine are available
#Sends pushover messages and Twilio texts with information
def notify(locs):
    message = 'Vaccine Appts Available at:\n'
    for name in locs:
        message = message + name + '\n'
    if(DEBUG):
        print(message)
    pushover(message)
    sendTexts(message)

#Sends texts to numbers in config['twilio']['numbers']
def sendTexts(message):
    client = Client(config['twilio']['acct_sid'],config['twilio']['auth_token'])
    for num in config['twilio']['numbers']:
        try:
            msg = client.messages.create(
                to=num,
                from_=config['twilio']['from_number'],
                body=message
            )
            if(DEBUG):
                print(msg.status)
        except TwilioRestException as err:
            print("Twilio Error, Run with \"debug:true\" for more details ")
            if(DEBUG):
                print(err)


#Sends pushover notifciations
def pushover(message):
    #Pushover Request
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": config['pushover']['api_key'],
        "user": config['pushover']['user_key'],
        "title" : "Vaccines Available!",
        "url" : "https://am-i-eligible.covid19vaccine.health.ny.gov/",
        "message": message,
        "priority" : 1
    })
    if r.status_code == 200:
        if DEBUG:
            print("Pushover Successful")
    else:
        print("Pushover Error, Run with \"debug:true\" for more details")
        if DEBUG:
            print(r.json())







#Loads Config file from CONFIG_FILE
def loadConfig(path):
    with open(path,'r') as f:
        return yaml.safe_load(f)

#Loads dict of locations to check
def loadLocations(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def main():
    #Load Config
    global config
    config = loadConfig(CONFIG_FILE)

    global DEBUG
    if('debug' in config):
        DEBUG = config['debug']
    else :
        DEBUG = False

    if(DEBUG):
        print("DEBUG MODE")
        pprint(config)

    #load locations to check
    to_check = loadLocations(LOCATIONS_FILE)

    #Pull Appts
    appts = getApptsTest()


    #Determine which Places have available locations
    availableLocs = availableLocations(to_check, appts)
    print("AVAILABLE LOCATIONS : " + str(availableLocs))
    #If Locations are available notify
    if(len(availableLocs) > 0):
        notify(availableLocs)

if __name__ == "__main__":
    main()
