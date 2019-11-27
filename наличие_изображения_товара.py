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
    image = browser.find_element_by_css_selector("div.item.active")
    assert image.is_displayed()
except NoSuchElementException:
    print("Image is not exist!")
finally:
    browser.quit()