from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/ru/"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_2 = browser.find_element_by_css_selector("[data-navigation = 'dropdown-menu'] > li:nth-child(1)")
    button_2.click()
    book = browser.find_element_by_css_selector('[title = "Hacking Exposed Wireless"]')
    book.click()
    price = browser.find_element_by_css_selector("[class = 'col-sm-6 product_main'] > [class = 'price_color']")
    assert price.is_displayed()
except NoSuchElementException:
    print('Price is not exist!')
finally:
    browser.quit()