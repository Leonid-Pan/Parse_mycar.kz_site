import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://mycar.kz/cars")
scroll_page = driver.execute_script("return document.body.scrollHeight")
button_cookie = driver.find_element(By.CLASS_NAME, 'text-uppercase.css-mz4xnw-Typography-interRegular-buttonSemibold14.e1c33kzw0')
button_cookie.click()
i = 0
while i < 2:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        newHeight = driver.execute_script("return document.body.scrollHeight")
        time.sleep(3)
        button = driver.find_element(By.CLASS_NAME, 'css-j91noz-Root.e7wkbvf0')
        button.click()
        time.sleep(2)
        i = i + 1
    except Exception as e:
        print("Error")
try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "css-1sg0nkn-CardResultCard-CarResultCardWrapperBase.elaysg91"))
    )
except Exception as e:
    print("Error")

cars = dict()
for elems in range(len(elements)):
    responce = elements[elems].text.split('\n')
    cars[elems] = responce

driver.close()
f = open('cars1.txt', 'w', encoding="utf-8")
print(cars)
for car in cars:
    f.write(str(cars[car])+"\n")
f.close()
