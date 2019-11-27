from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button_2 = browser.find_element_by_css_selector("[data-navigation = 'dropdown-menu'] > li:nth-child(1)")
    button_2.click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = browser.find_element_by_css_selector("li.next a")
    assert button.is_displayed()
except NoSuchElementException:
    print("Button 'Вперёд' is not exist!")
finally:
    browser.quit()