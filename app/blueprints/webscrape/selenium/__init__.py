from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

def repeatableAction(browserObj):
    browserObj.find_element_by_id("search").send_keys("dwight howard, lebron james, giannis antetokounmpo, chris paul, kemba walker, james harden")
    sleep(2)

    browserObj.find_element_by_id("search").send_keys(Keys.ENTER)
    sleep(2)

    submitCSVButton = browserObj.find_element_by_id("submitCSV")
    action = ActionChains(browserObj)
    action.click(submitCSVButton)
    action.perform()
    sleep(10)

def execute():
    chrome_options = webdriver.ChromeOptions()
    # print(os.path.join(os.path.dirname(__file__), 'chromedriver'))
    browser = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), 'chromedriver'), chrome_options=chrome_options)
    browser.maximize_window()
    sleep(3)

    browser.get('localhost:5000/webscrape')
    sleep(3)

    for i in range(10):
        repeatableAction(browser)
    # repeatableAction(browser)

    browser.quit()

