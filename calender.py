### This is the program for recieve the important news from "Farex Factory" ###

# import requests, json , bs4 , re

from socketserver import DatagramRequestHandler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
PATH = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe' 

driver = webdriver.Chrome(PATH)

driver.get("")

print(driver.title)

search = driver.find_element(by=By.NAME, value="search")
driver.quit()