from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    c = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(c)
    checkbox = browser.find_element_by_css_selector('div div:nth-child(2)>input')
    checkbox.click()
    time.sleep(1)
    radio = browser.find_element_by_id('robotsRule') 
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    time.sleep(1)
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    alert=browser.switch_to_alert()
    print (alert.text)
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла