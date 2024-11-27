import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import json

# чтобы не передавать в git мои логин/пароль, в проекте предварительно создала json файл 'config.json'
    # и добавила его в файл gitignore.py
    # импортируем библиотеку json и создаем фикстуру, которая вернет словарь логин/пароль из файла config.json:
@pytest.fixture(scope="session")
def load_config():
    # Открываем файл 'config.json' с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        # вернуть словарь из логина и пароля
        return config

    # введем переменную для дальнейшей конкатенации кусочков ответа
message = ''
        # в качестве аргументов передаётся изменяемая часть ссылок
@pytest.mark.parametrize('part_of_link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_links(browser, load_config, part_of_link):
    answer = math.log(int(time.time()))
    browser.get(f'https://stepik.org/lesson/{part_of_link}/step/1')
        # вводим результат answer в поле ввода
    enter_field = browser.find_element(By.CSS_SELECTOR, '.string-quiz__textarea')
    enter_field.clear()
    enter_field.send_keys(str(answer))
        # кликаем по кнопке Отправить
    send_button_field = (By.CSS_SELECTOR, '.st-link.st-link_style_button')
    send_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(send_button_field))
    send_button.click()
        # записываем в переменные логин/пароль
    login = load_config['login_stepik']
    password = load_config['password_stepik']
        # находим поле логина и вводим его
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
        # находим поле пароля и вводим его
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
        # находим кнопку Войти и кликаем по ней
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
        # лицезреть действия
    time.sleep(2)
    result = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint'))).text
    # для красивой записи ответа использовала оператор if, чтобы ответ был в строчку и его не искать по упавшим тестам
    # assert result == 'Correct!', f'message is:   {result}'
        # указываем global - ранее заведенную переменную, чтобы использовать ее в этой функции
    global message
    if result != 'Correct!':
        message += result
        print(f'\ntext for answer:   {message}')








