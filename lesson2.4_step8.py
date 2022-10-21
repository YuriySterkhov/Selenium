from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    #browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, "book")
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text    
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    button = browser.find_element(By.XPATH, "//button[@type='submit']")   
    button.click()

   # message = browser.find_element(By.ID, "verify_message")

   # assert "successful" in message.text
    

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла