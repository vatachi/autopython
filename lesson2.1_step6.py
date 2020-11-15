from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element_by_tag_name("img")
    key = box.get_attribute("valuex")
    #x = key.text
    c = calc(key)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(c)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    alert=browser.switch_to_alert()
    print (alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла