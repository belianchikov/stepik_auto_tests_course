from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
	
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)
	submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
	submit.click()
	pop = prompt = browser.switch_to.alert
	pop.accept()
	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x=calc(x_element.text)
	input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
	input_field.send_keys(x)
	submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
	submit.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()