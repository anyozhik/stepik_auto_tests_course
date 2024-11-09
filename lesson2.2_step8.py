from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    labels =['Ivan', 'Ivanov', 'ivanov@gmail.com']

    inputs=browser.find_elements(By.CSS_SELECTOR, "input[type='text'][required]")

    for input, label in zip(inputs, labels):
        input.send_keys(label);

    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


    #Заметки по загрузке файла. При использовнаии jupiter notebook: нужны кавычки os.path.dirname('__file__'). Файл должен лежать: C:\Users\apach\file.txt 

