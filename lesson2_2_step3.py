from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    first = int(num1.text)
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    second = int(num2.text)
    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropdown.select_by_value(str(first+second))


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()