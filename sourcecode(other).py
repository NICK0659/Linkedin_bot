import pandas as pd
from parsel import selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts=Options()

driver= webdriver.Chrome(options=opts, executable_path='chromedriver')
# function to ensure all key data fields have a value 
def validate_field(field):
    #if field is present pass if field:
    if field:
        pass
    #if field is not present print text else:
    else:
        field='No results'
    return field

#driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

#locate email from by_class_name
username=driver.find_element(By.ID,'session_key')

#send_keys() to simulate the key strokes
username.send_keys('YOUR EMAIL')

#sleep for 0.5 seconds
sleep(0.5)

#locate password from by_class_name
password=driver.find_element(By.ID,'session_passsword')

#send_keys() to simulate the key strokes
password.send_keys('YOUR PASSWORD')

#sleep for 0.5 seconds
sleep(0.5)

#locate submit button by_xpath
sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

#.click() to mimic button click 
sign_in_button.click()
sleep(15)


