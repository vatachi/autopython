from selenium import webdriver
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_xpath('//input[@name="firstname"]')
    input_name.send_keys("Имя")
    input_last_name = browser.find_element_by_xpath('//input[@name="lastname"]')
    input_last_name.send_keys("Фамилия")
    input_email = browser.find_element_by_xpath('//input[@name="email"]')
    input_email.send_keys("123@MAIL.RU")
    but_load = browser.find_element_by_xpath('//input[@type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')
    but_load.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    alert=browser.switch_to_alert()
    print (alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла