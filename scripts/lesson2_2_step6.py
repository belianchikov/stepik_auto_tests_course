from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x=x_element.text
    input1 = browser.find_element(By.CSS_SELECTOR,"#answer")
    input1.send_keys(str(calc(int(x))))
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    input2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    input2.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()