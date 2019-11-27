from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_1 = browser.find_element_by_id("id_q")
    input_1.send_keys("Hacking Exposed Wireless")
    button_1 = browser.find_element_by_css_selector("[value = 'Найти']")
    button_1.click()
    product = browser.find_element_by_css_selector("[title = 'Hacking Exposed Wireless']")
    assert product.is_enabled()
except NoSuchElementException:
    print('Button "Найти" is not work correctly!')
finally:
    browser.quit()