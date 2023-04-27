from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://chromedriver.chromium.org/home")

# поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, '//div/a/img')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')