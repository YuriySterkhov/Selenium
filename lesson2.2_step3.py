from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)

    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    z = x + y
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z)) 
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла