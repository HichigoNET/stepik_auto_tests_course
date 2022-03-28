from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://SunInJuly.github.io/execute_script.html")
    button = driver.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view
    button.click()
    assert True
finally:
    driver.quit()
    