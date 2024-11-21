from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Переключиться на новую вкладку (сначала определяем переменную, потом на нее переключаемся)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # На новой вкладке решить капчу для роботов, чтобы получить число с ответом
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



