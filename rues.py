import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = 'C:\\projects\\scrapring_rues\\driver\\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
url = "https://www.rues.org.co/"
driver.get(url)

time.sleep(5)


boton_cerrar = driver.find_element(By.CLASS_NAME, "btn-success")
boton_cerrar.click()

driver.find_element(By.ID, 'txtNIT').clear()
nit = driver.find_element(By.ID, 'txtNIT')
nit.send_keys('900866992')

boton_cerrar = driver.find_element(By.ID, "btnConsultaNIT")
boton_cerrar.click()


time.sleep(5)
driver.close()
