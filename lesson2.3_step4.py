from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Принять confirm
    confirm=browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element=browser.find_element(By.CSS_SELECTOR, '#input_value')
    x=x_element.text
    y=calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



