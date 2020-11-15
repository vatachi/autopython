from selenium import webdriver
import os


link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    browser.find_element_by_id("button")



finally:
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла