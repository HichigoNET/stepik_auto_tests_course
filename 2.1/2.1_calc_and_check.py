import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/math.html")
    #el =browser.find_element_by_id("input_value")
    #x = el.text
    #calc(browser.find_element_by_id("input_value").text())
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector("[for=\"robotCheckbox\"]").click()
    browser.find_element_by_css_selector("[for=\"robotsRule\"]").click()
    browser.find_element_by_css_selector("[type=\"submit\"]").click()
finally:
    browser.quit()
