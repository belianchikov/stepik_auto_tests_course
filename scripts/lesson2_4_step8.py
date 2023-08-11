from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button = browser.find_element(By.ID, "book")
button.click()
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x=calc(x_element.text)
input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
input_field.send_keys(x)
submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()