import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dados import dadosCNPJ
from utils.fotinha import TiraFoto

url = "https://user_inmetrics09:Xiaomi_v3290@trbnethml.tribanco.com.br/Tribanco.BoletaUnica.WebUI.V2/ConsConsultaGeral.aspx"

driver = webdriver.Chrome('../utils/chromedriver.exe')
driver.implicitly_wait(45)
photo = TiraFoto(driver, 'XPTO-1004')


def begin():

    driver.maximize_window()
    driver.get(url)
    print('\033[36m' + 'Acessou o site.\033[0;0m')
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT, 'Nova Solicitação').click()
    driver.find_element(By.ID, 'MainContent_txtCnpjCpf').send_keys(dadosCNPJ.cnpj)
    driver.find_element(By.LINK_TEXT, 'Pesquisar').click()
    familia = Select(driver.find_element(By.ID, 'MainContent_lstFamilia'))
    familia.select_by_value(dadosCNPJ.familiaCod)
    time.sleep(1)
    photo.tira_foto()
    produto = Select(driver.find_element(By.ID, 'MainContent_lstProduto'))
    produto.select_by_value(dadosCNPJ.produtoCod)
    time.sleep(1)
    photo.tira_foto()
    modalidade = Select(driver.find_element(By.ID, 'MainContent_lstModalidade'))
    modalidade.select_by_value(dadosCNPJ.modalidadeCod)
    time.sleep(1)
    photo.tira_foto()
    evento = Select(driver.find_element(By.ID, 'MainContent_lstEvento'))
    evento.select_by_value(dadosCNPJ.eventoCod)
    time.sleep(2)
    photo.tira_foto()


photo.criaDiretorio()
while not photo.criaSubpasta():
    print('\033[32m' + 'Criando outra pasta')
begin()
