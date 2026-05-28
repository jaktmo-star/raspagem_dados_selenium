from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# drive do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# url
url = 'https://www.amazon.com.br/dp/B0DYVPCX34'

# abrir site
driver.get(url)
time.sleep(60)

# mostrar dados
inteiro = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
decimal = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text

print (f'Preço: R${inteiro},{decimal}')

driver.quit()