import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    #el =browser.find_element_by_id("input_value")
    #x = el.text
    #calc(browser.find_element_by_id("input_value").text())
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("treasure").get_attribute("valuex")))
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("[type=\"submit\"]").click()
finally:
    browser.quit()
