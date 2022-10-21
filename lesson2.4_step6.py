from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element(By.ID, "button")
    

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла