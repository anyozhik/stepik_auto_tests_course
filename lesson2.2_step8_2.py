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

    # попробуем "на лету создать файл"

    with open('test1.txt', 'w') as file:
        file.write('test1 for mls 228')

    # файл сразу после записи в него строки "test1 for mls 228" закроется, а вот переменная file будет содержать всю нужную информацию, в частности, file.name будет содержать имя файла

    ospath = os.getcwd() + '/' + file.name   

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(ospath)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    os.remove('test1.txt')


