import time
import sys
from scenarios import login
from dados import dadosCadastro
from uimaps import cadastroMap
from selenium.webdriver.common.by import By
from utils.fotinha import TiraFoto

driver = login.driver
foto = TiraFoto(driver, 'Proposta')


def criaProp():
    print('\033[32m'+'Fechando pop-up'+'\033[0;0m')
    '''driver.switch_to.window(driver.window_handles[1])
    driver.close()'''
    driver.find_element(By.CSS_SELECTOR, "[alt = 'proposta online']").click()


def preenchProp():
    driver.find_element(By.ID, 'ctl00_body_txtNomeCompleto').send_keys(dadosCadastro.nomeCompleto)
    driver.find_element(By.ID, 'ctl00_body_txtCpf').send_keys(dadosCadastro.cpf)
    driver.find_element(By.ID, 'ctl00_body_txtdataNascimento').send_keys(dadosCadastro.dtNsc)
    driver.find_element(By.ID, 'ctl00_body_txtEmail').send_keys(dadosCadastro.email)
    driver.find_element(By.ID, 'ctl00_body_txtDDDPessoal').send_keys(dadosCadastro.ddd)
    driver.find_element(By.ID, 'ctl00_body_txtTelefonePessoal').send_keys(dadosCadastro.cel)
    time.sleep(3)
    driver.find_element(By.ID, 'ctl00_body_dddConfirmacao').send_keys(dadosCadastro.ddd)
    driver.find_element(By.ID, 'ctl00_body_telefoneConfirmacao').send_keys(dadosCadastro.cel)
    foto.tira_foto()
    driver.find_element(By.ID, 'btnSalvar').click()
    driver.find_element(By.CSS_SELECTOR, cadastroMap.botao).click()
    time.sleep(5)
    foto.tira_foto()
    jaTem = input('\033[1;93m' + '\033[1;100m' + 'Já possui proposta? (Digite n para continuar)\033[0;0m\n')
    if jaTem.upper() == 'N':
        return True
    else:
        driver.quit()
        sys.exit()
