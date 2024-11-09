rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    #Нажать на кнопку "Book"
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
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

