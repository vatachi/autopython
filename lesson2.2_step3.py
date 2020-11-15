from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    ch1 = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    ch2 = int(num2.text)
    rez = ch1 + ch2
    rez=str(rez)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(rez)
    button = browser.find_element_by_class_name("btn")
    button.click()
    
finally:
    alert=browser.switch_to_alert()
    print (alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла