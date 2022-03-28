from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
try:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WDW(driver,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button = driver.find_element_by_css_selector("#book")
    driver.execute_script("return arguments[0].scrollIntoView(true);",button)
    button.click()
    #driver.execute_script("return arguments[0].scrollIntoView(true);",price_text_field)
    answer = driver.find_element_by_id("answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);",answer)
    answer.send_keys(calc(driver.find_element_by_id("input_value").text))

    btn = driver.find_element_by_xpath("//button[@type=\"submit\"]")
    driver.execute_script("return arguments[0].scrollIntoView(true);",btn)
    btn.click()

finally:
    driver.quit()
