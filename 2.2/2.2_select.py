from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/selects2.html")
    res = str(int(browser.find_element_by_id("num1").text)+int(browser.find_element_by_id("num2").text))
    Select(browser.find_element_by_tag_name("select")).select_by_value(res)
    browser.find_element_by_css_selector("[type=\"submit\"]").click()
finally:
    browser.quit()
