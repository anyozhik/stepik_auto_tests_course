from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    
    # Вводим ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # Отметить checkbox "I'm the robot".
    browser.find_element(By.CSS_SELECTOR, '.form-check-input[type="checkbox"]').click()

    #Выбрать radiobutton "Robots rule!" (он перекрыт футером!)
    button=browser.find_element(By.CSS_SELECTOR, ".form-check-input[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    #Нажать на кнопку Submit. (она перекрыта футером!)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
# print(browser.switch_to.alert.text.split()[-1])
