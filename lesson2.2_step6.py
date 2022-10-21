from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text    
    y = calc(x)
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("window.scrollBy(0, 100);")

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    
    button.click()    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла