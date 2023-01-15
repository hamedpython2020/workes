 ### This is the program for recieve the important news from "Farex Factory" ###

# import requests, json , bs4 , re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://vu.um.ac.ir/login/index.php")

print(driver.title)

search_user = driver.find_element(by=By.ID, value="username")
search_pass = driver.find_element(by=By.ID, value="password")
search_login = driver.find_element(by=By.ID, value="loginbtn")
search_user.send_keys("9912742509")
search_pass.send_keys("hamed2018")
search_login.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'courses-view-630cd9fc542bd630cd9fc13cdd6'))
    )
# main = driver.find_element(by=By.ID, value='courses-view-630cd9fc542bd630cd9fc13cdd6')
    courses = main.find_element(By.TAG_NAME, 'h6')
    for course in courses:
        print(course.text, '\n')
finally:
    driver.quit()

