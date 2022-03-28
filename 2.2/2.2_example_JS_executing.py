from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.execute_script("document.title=\"Script executing\";alert(\"Robots at work\")")
finally:
    browser.quit()
