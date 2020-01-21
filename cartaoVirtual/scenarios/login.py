from selenium import webdriver
from selenium.webdriver.common.by import By
from dados import dadosLogin
from utils.fotinha import TiraFoto


url = 'https://hml11.tricardonline.com.br/ParaSuaLoja/login_intranet.aspx'


driver = webdriver.Chrome('../utils/chromedriver.exe')
driver.implicitly_wait(25)
foto = TiraFoto(driver, 'Login')


def inicio():
    driver.maximize_window()
    driver.get(url)
    print('\033[36m' + 'Acessou o site.\033[0;0m')


def logar():
    print('\033[1;32m' + 'Efetuando login.\033[0;0m')
    foto.tira_foto()
    driver.find_element(By.ID, 'login').send_keys(dadosLogin.usr)
    driver.find_element(By.ID, 'senha').send_keys(dadosLogin.pw)
    driver.find_element(By.ID, 'codigotricard').send_keys(dadosLogin.loja)
    foto.tira_foto()
    driver.find_element(By.ID, 'LogarIntranet').click()
    foto.tira_foto()
