from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

