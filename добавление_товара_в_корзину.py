from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/ru/"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    log_in = browser.find_element_by_id("login_link")
    log_in.click()
    input_1 = browser.find_element_by_name("login-username")
    input_1.send_keys("adeliya.abushakhmanova@gmail.com")
    input_2 = browser.find_element_by_name("login-password")
    input_2.send_keys("stepikfirst01")
    button_1 = browser.find_element_by_name("login_submit")
    button_1.click()
    button_2 = browser.find_element_by_css_selector("[data-navigation = 'dropdown-menu'] > li:nth-child(1)")
    button_2.click()
    book = browser.find_element_by_css_selector('[title = "Hacking Exposed Wireless"]')
    book.click()
    add_button = browser.find_element_by_css_selector('[value = "Добавить в корзину"]')
    add_button.click()
    button_3 = browser.find_element_by_css_selector("[class = 'alertinner '] a:nth-child(1)")
    button_3.click()
    product = browser.find_element_by_css_selector("[href = '/ru/catalogue/hacking-exposed-wireless_208/']")
    assert product.is_displayed()
except NoSuchElementException:
    print("Товар не добавлен в корзину")
finally:
    browser.quit()
