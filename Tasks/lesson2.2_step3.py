from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time





try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    f_element= browser.find_element(By.CSS_SELECTOR, '#num1').text
    s_element= browser.find_element(By.CSS_SELECTOR, '#num2').text
    total_sum=int(f_element)+int(s_element)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total_sum)) # ищем элемент со значением value=total_sum
    

    #Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
