from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.alert.accept()
    browser.find_element_by_id("answer").send_keys(calc(browser.find_element_by_id("input_value").text))
    #browser.find_element(By.XPATH,"//button[@type=\"submit\"]").click()
    browser.find_element_by_xpath("//button[@type=\"submit\"]").click()

finally:
    browser.quit()
