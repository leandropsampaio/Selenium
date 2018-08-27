from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

rolarPagina = "500"

print("Teste automatizado iniciado!")

driver = webdriver.Chrome("C:\\Users\\Micro\\Downloads\\chromedriver_win32\\chromedriver.exe") # Adicionar o navegador
driver.get("http://www.google.com") # Abrir o site da Google no navegador

#wait = WebDriverWait(driver, 10)

assert "Google" in driver.title # Verificar o título da página se é "Google"

''' Maneiras de encontrar um elemento
EX: <input type="text" name="passwd" id="passwd-id" />

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
'''

elemento = driver.find_element_by_xpath("//div[2]/div/input")
#elemento = driver.find_element_by_name("q") # Procurar elemento na página
elemento.clear() # Limpar elemento
elemento.send_keys("facebook") # Escrever no elemento

elemento = driver.find_element_by_name("btnK").click()
#elemento.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0, "+ rolarPagina +");")
#driver.save_screenshot('screenshot.png') # Tirar print da tela e salva na área de trabalho

assert "No results found." not in driver.page_source

#driver.close() # Fechar o navegador

print("Teste automatizado finalizado!")