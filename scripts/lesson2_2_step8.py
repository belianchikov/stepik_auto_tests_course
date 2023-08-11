from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, '../file.txt')           # добавляем к этому пути имя файла
	print(file_path)
	print(os.path.abspath(__file__))
	print(os.path.abspath(os.path.dirname(__file__)))
	firstname_input = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
	firstname_input.send_keys("123")
	lastname_input = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
	lastname_input.send_keys("123")
	email_input = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
	email_input.send_keys("123")
	attach = browser.find_element(By.CSS_SELECTOR,'[type="file"]')
	attach.send_keys(file_path)
	submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
	submit.click()
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()