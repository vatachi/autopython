from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("t")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    alert=browser.switch_to_alert() 
    print (alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла