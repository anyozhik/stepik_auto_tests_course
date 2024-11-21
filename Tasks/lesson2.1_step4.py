from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    
    # Вводим ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # Отметить checkbox "I'm the robot".
    browser.find_element(By.CSS_SELECTOR, '.form-check-input[type="checkbox"]').click()

    #Выбрать radiobutton "Robots rule!".
    browser.find_element(By.CSS_SELECTOR, ".form-check-input[id='robotsRule']").click()

    #Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
