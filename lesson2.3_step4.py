from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    c = calc(x)
    input = browser.find_element_by_class_name('form-control')
    input.send_keys(c)
    button = browser.find_element_by_class_name("btn")
    button.click() 
    
finally:
    alert = browser.switch_to.alert
    print(alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла