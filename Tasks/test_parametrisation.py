import pytest
import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# импортируем библиотеку и создаем фикстуру:
@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config=json.load(config_file)
        return config
        
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test 'Parametrisation'")
    browser=webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


#передаем результаты в тестируемую функцию состояние фикстур таких как браузер:
class TestLoginStepik:
    def test_authorization(self, browser, load_config):
        login=load_config['login_stepik']
        password=load_config['password_stepik']
        link='https://stepik.org/lesson/236895/step/1'
        browser.get(link)
        time.sleep(20)
        button=browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login")
        button.click()
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()
        
        

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
    # link=f"http://selenium1py.pythonanywhere.com/{language}/"
   # browser.get(link)
   # browser.find_element(By.CSS_SELECTOR, "#login_link")
