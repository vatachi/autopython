from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    book = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(price)
    book.click()
    
    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    c=calc(x)
    
    input = browser.find_element(By.CLASS_NAME, 'form-control')
    input.send_keys(c)
    
    browser.find_element(By.ID, 'solve').click()

finally:
    alert=browser.switch_to_alert()
    print (alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
# не забываем оставить пустую строку в конце файла