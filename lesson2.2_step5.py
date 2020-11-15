from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector(#input_value)
    #x = x_element.text
    print(x_element)
    #c = calc(x)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла