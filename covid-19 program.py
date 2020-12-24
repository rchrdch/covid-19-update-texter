from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random, schedule, time
from twilio.rest import Client

url = 'https://app.powerbi.com/view?r=eyJrIjoiMzI4OTBlMzgtODg5MC00OGEwLThlMDItNGJiNDdjMDU5ODhkIiwidCI6ImQ1N2QzMmNjLWMxMjEtNDg4Zi1iMDdiLWRmZTcwNTY4MGM3MSIsImMiOjN9'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = #enter path to chrome driver
driver = webdriver.Chrome(options = options, executable_path = DRIVER_PATH)
driver.get(url)
driver.page_source
driver.implicitly_wait(10)

num = driver.find_element_by_xpath('/html/body/div[1]/ui-view/div/div[1]/div/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[8]/transform/div/div[3]/div/visual-modern/div/div/div/div[1]/div/div/div/div/div[3]/div[1]').text
date = driver.find_elements_by_css_selector('#pvExplorationHost > div > div > exploration > div > explore-canvas-modern > div > div.canvasFlexBox > div > div.displayArea.disableAnimations.fitToWidthOrigin > div.visualContainerHost > visual-container-repeat > visual-container-modern:nth-child(11) > transform > div > div:nth-child(3) > div > visual-modern > div > svg > g:nth-child(1) > text > tspan')
for x in date:
    date = x.text
    # print(date)
driver.quit()

covid_cellphones = [#enter cellphone numbers here]

twilio_num = #enter twilio number here

def send_covid_text(message):
    account = #enter twilio account number here
    token = #enter twilio API token here
    client = Client(account, token)

    for i in covid_cellphones:
        client.messages.create(to = i,
                            from_ = twilio_num,
                            body = "Automated Covid-19 Program: " + message)

message2 = "There were " + num + " positive tests on " + date + " at Boston University. Don't forget to wear a mask to save lives!"
schedule.every().day.at("14:00").do(send_covid_text, message2)

while True:
    schedule.run_pending()
    time.sleep(2)
