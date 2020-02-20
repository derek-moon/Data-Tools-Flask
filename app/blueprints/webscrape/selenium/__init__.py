from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


def execute():
    chrome_options = webdriver.ChromeOptions()

    browser = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__),'chromedriver'),chrome_options=chrome_options)
    
    browser.get('localhost:5000/')
    

