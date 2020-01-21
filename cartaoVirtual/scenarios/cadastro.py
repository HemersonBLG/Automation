import time
from scenarios import login
from dados import dadosCadastro
from uimaps import cadastroMap
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.fotinha import TiraFoto

driver = login.driver
foto = TiraFoto(driver, 'Cadastro')


def finalProp():
    foto.tira_foto()
    driver.find_element(By.ID, 'ctl00_body_txtrg').send_keys(dadosCadastro.RG)
    driver.find_element(By.ID, 'ctl00_body_txtOrgaoEmissor').send_keys(dadosCadastro.orgEmiss)
    driver.find_element(By.ID, 'ctl00_body_txtdataEmissao').send_keys(dadosCadastro.dtEmiss)
    driver.find_element(By.ID, 'ctl00_body_txtNaturalidade').send_keys(dadosCadastro.nat)
    muni = Select(driver.find_element(By.ID, 'ctl00_body_ddlUf'))
    muni.select_by_value(dadosCadastro.uf)
    nac = Select(driver.find_element(By.ID, 'ctl00_body_ddlNacionalidade'))
    nac.select_by_value('1')
    gen = Select(driver.find_element(By.ID, 'ctl00_body_ddlGenero'))
    gen.select_by_value('M')
    driver.find_element(By.ID, 'ctl00_body_txtNomeMae').send_keys(dadosCadastro.nomeMae)
    driver.find_element(By.ID, 'ctl00_body_txtCep').send_keys(dadosCadastro.cep)
    time.sleep(2)
    foto.tira_foto()
    validaEnd = driver.find_element(By.ID, 'ctl00_body_txtEndereco').text
    print(validaEnd)
    if validaEnd == '':
        driver.find_element(By.ID, 'ctl00_body_txtEndereco').send_keys(dadosCadastro.end)
    time.sleep(2)
    driver.find_element(By.ID, 'ctl00_body_txtNumero').send_keys(dadosCadastro.numEnd)
    # comp = Select(driver.find_element(By.ID, 'ctl00_body_ddlComplemento'))
    # comp.select_by_value('CS')
    driver.find_element(By.CSS_SELECTOR, cadastroMap.profissa).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, cadastroMap.profissa).send_keys(dadosCadastro.pro)
    driver.find_element(By.CSS_SELECTOR, cadastroMap.profissa).send_keys(Keys.TAB)
    driver.find_element(By.ID, 'ctl00_body_ddlNaturezaProf').send_keys(dadosCadastro.natPro)
    driver.find_element(By.ID, 'ctl00_body_txtSalarioProf').send_keys(dadosCadastro.renda)
    dtVenc = Select(driver.find_element(By.ID, 'ctl00_body_ddlVencimentoCartao'))
    dtVenc.select_by_value('15')
    foto.tira_foto()
    driver.find_element(By.ID, 'ctl00_body_txtEmailConfirmacao').send_keys(dadosCadastro.email)
    driver.find_element(By.ID, 'ctl00_body_txtNomeRef1').send_keys(dadosCadastro.nomeRef)
    driver.find_element(By.ID, 'ctl00_body_txtDDDRef1').send_keys(dadosCadastro.dddRef)
    driver.find_element(By.ID, 'ctl00_body_txtTelefoneRef1').send_keys(dadosCadastro.celRef)
    driver.find_element(By.ID, 'ctl00_body_chkTermoResp').click()
    foto.tira_foto()
    driver.find_element(By.ID, 'btnSalvar').click()
    print(driver.find_element(By.CSS_SELECTOR, cadastroMap.finaliza))
    print(driver.find_element(By.CSS_SELECTOR, 'button'))
    print(driver.find_element(By.CSS_SELECTOR, 'button').get_attribute('textContent'))
    print(driver.find_element(By.CSS_SELECTOR, cadastroMap.finaliza).get_attribute('textContent'))
