from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.get("https://suninjuly.github.io/execute_script.html")
    btn=browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);",btn)
    btn.click()
finally:
    browser.quit()
    