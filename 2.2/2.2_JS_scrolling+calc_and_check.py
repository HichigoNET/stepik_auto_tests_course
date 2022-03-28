from selenium import webdriver
from math import *

def calc(x):
    return str(log(abs(12*sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/execute_script.html")
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector("[for=\"robotCheckbox\"]").click()
    rbtn=browser.find_element_by_css_selector("[for=\"robotsRule\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);",rbtn)
    rbtn.click()
    btn=browser.find_element_by_css_selector("[type = \"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);",btn)
    btn.click()
finally:
    browser.quit()
