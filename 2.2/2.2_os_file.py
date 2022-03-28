import os
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/file_input.html")
    #текущая папка скрипта
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path =os.path.join(dir_path,"file.txt")
    els = browser.find_elements(By.CSS_SELECTOR,"div.form-group > input")
    for el in els:
        #el.send_keys("1")
        el.send_keys(el.get_attribute("placeholder"))
    file_btn = browser.find_element_by_xpath("//input[@type=\"file\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);",file_btn)
    file_btn.send_keys(file_path)
    btn = browser.find_element_by_class_name("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);",btn)
    btn.click()
finally:
    browser.quit()