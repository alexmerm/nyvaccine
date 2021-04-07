from selenium.webdriver import Chrome,DesiredCapabilities,Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from fake_useragent import UserAgent
import json
from pprint import pprint

START_PAGE = "https://www.cvs.com/immunizations/covid-19-vaccine"
INFO_URL = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.NY.json?vaccineinfo"

SELENIUM_URL = "http://192.168.0.57:4444/wd/hub"

#https://github.com/SeleniumHQ/selenium/issues/8672
def cdp_cmd(driver, cmd, params={}):
  resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
  url = driver.command_executor._url + resource
  body = json.dumps({'cmd': cmd, 'params': params})
  response = driver.command_executor._request('POST', url, body)
  return response.get('value')

def getCvsStatus():
    #Use fake useragent
    options = Options()
    ua = UserAgent()
    userAgent = ua.Chrome
    #print(userAgent)
    #Enable Logging 
    options.add_argument(f'user-agent={userAgent}')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['goog:loggingPrefs'] = {
        'browser': 'ALL',
        'performance' : 'ALL',
        'network' : 'ALL'
    }
    #print(capabilities)
    with Remote(command_executor=SELENIUM_URL, options=options, desired_capabilities=capabilities,) as driver:
        #Set Window to random Size
        driver.set_window_size(random.randint(1201,1400), random.randint(1000,1300))
        wait = WebDriverWait(driver,20)
        #store window of locations page
        firstPage = driver.get(START_PAGE)
        sleep(1)
        nyLink = driver.find_element(By.XPATH,"//a[@data-modal='vaccineinfo-NY']")
        wait = WebDriverWait(driver,20)
        driver.execute_script("arguments[0].scrollIntoView();",nyLink)
        wait.until(EC.visibility_of(nyLink))
        sleep(1)
        ActionChains(driver).move_to_element(nyLink).click(nyLink).perform()
        sleep(5)
        #Can check for visibility of ny data modal thing but im not going to 
        #Now to log
        perfs = driver.get_log('performance')
        for line in perfs:
            event = json.loads(line['message'])['message']
            if 'Network.response' in event['method']:
                #pprint(event, depth=10)
                reqId = event["params"]["requestId"]
                if "response" in event["params"]:
                    if event["params"]["response"]["url"] == "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.NY.json?vaccineinfo":
                        idOfVaxReq = reqId
        vaxReqResp = json.loads(cdp_cmd(driver,'Network.getResponseBody', {'requestId': idOfVaxReq})["body"])
        pprint(vaxReqResp)
        payload = vaxReqResp['responsePayloadData']
        asOfTime = payload['currentTime']
        print(" As of " + asOfTime)
        cities = payload['data']['NY']
        for city in cities:
            print(city)
        print("Done")
        #driver.quit() I think this is done by the "with" statemenbt
        return asOfTime, cities
def main():
    asOfTime,cities = getCvsStatus()
    print(asOfTime)
    pprint(cities)
main()