from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_checking_button_for_basket(browser):
    browser.get(link)
    time.sleep(30)
    
    try:
        basket_button=browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    except:
        assert False, "Button is not found"


