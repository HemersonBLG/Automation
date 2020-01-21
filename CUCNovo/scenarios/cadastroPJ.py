from scenarios import login
from dados import dadosPJ
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.screenshot import TakeShoot
from utils.saveCPF import Grava
import time

pj = dadosPJ
driver = login.driver
photo = TakeShoot(driver, 'TESTE')
photo.createDiretory()
while not photo.createSubPaste():
    print('\033[32m' + 'Criando outra pasta')


def cadPJ():
    driver.find_element(By.ID, 'btnCadastrar').click()

    photo.takeShot()

    driver.find_element(By.LINK_TEXT, 'PJ').click()


def insereDados():

    photo.takeShot()

    nv = input('Qual o nível de preenchimento?\n'
               '1 - Nível 1\n'
               '2 - Nível 2\n'
               '3 - Nível 3\n')

    log = Grava('2', nv, pj.cnpj)

    def nv1():
        time.sleep(3)

        photo.takeShot()

        driver.find_element(By.ID, 'ucPessoaPJ1_txtCnpjPJ').send_keys(pj.cnpj)
        driver.find_element(By.ID, 'ucPessoaPJ1_txtRazaoSocialPJ').send_keys(pj.razaoSocial)
        catMartins = Select(driver.find_element(By.ID, 'ddlCategoriaPJ'))
        catMartins.select_by_value('12')

        photo.takeShot()

    def nv2():
        driver.find_element(By.ID, 'ucPessoaPJ1_txtNomeFantasiaPJ').send_keys(pj.nomeFantasia)

        tipoEmpresa = Select(driver.find_element(By.ID, 'ucPessoaPJ1_ddlTipoEmpresaPJ'))
        tipoEmpresa.select_by_value('4')
        ramoEmpresa = Select(driver.find_element(By.ID, 'ucPessoaPJ1_ddlRamoAtividadePJ'))
        ramoEmpresa.select_by_value('49')
        paisConstituicao = Select(driver.find_element(By.ID, 'ddlPaisConstituicao'))
        paisConstituicao.select_by_value('105')
        paisDomicilio = Select(driver.find_element(By.ID, 'ddlPaisDomicilioFiscal'))
        paisDomicilio.select_by_value('105')

        photo.takeShot()

        driver.find_element(By.ID, 'ucPessoaPJ1_txtNumCnaePJ').send_keys(pj.cnae)
        driver.find_element(By.ID, 'btnPesquisarCnae').click()

        time.sleep(1)
        driver.find_element(By.ID, 'ucEndereco2_txtCEPSede').send_keys(pj.pjCep)
        driver.find_element(By.ID, 'btnPesquisarCEPSede').click()
        driver.find_element(By.ID, 'ucEndereco2_txtNumeroSede').send_keys(pj.pjNumCasa)
        driver.find_element(By.ID, 'rbEndInternacionalFalsePJ').click()
        time.sleep(1)
        photo.takeShot()
        print('Nível ' + nv)

    def nv3():
        # Contact Include
        driver.find_element(By.CSS_SELECTOR, "[data-target='#addContato']").click()
        driver.find_element(By.ID, 'txtNomeCtto').send_keys(pj.contatoNome)
        relacao = Select(driver.find_element(By.ID, 'ddlRelacaoCargoCtto'))
        relacao.select_by_value('14')
        tipoContato = Select(driver.find_element(By.ID, 'ddlMeioComunicacaoCtto'))
        tipoContato.select_by_value('3')
        driver.find_element(By.ID, 'txtDescComunicacaoCtto').send_keys(pj.contatoTelefone)
        time.sleep(1)

        photo.takeShot()

        driver.find_element(By.ID, 'btnInserirContato').click()

        # Comertial Reference
        driver.find_element(By.CSS_SELECTOR, "[data-target='#addRefComercial']").click()
        driver.find_element(By.ID, 'txtRazaoSocialCom').send_keys(pj.empresaNome)
        driver.find_element(By.ID, 'txtTelefoneCom').send_keys(pj.empresaCel)
        photo.takeShot()
        driver.find_element(By.ID, 'btnInserirRefComercial').click()

        # Scenarios Fincial
        time.sleep(1)
        driver.find_element(By.ID, 'ucCenarioFinanceiro2_txtQt_Empregado').send_keys(pj.qtdEmpregados)
        driver.find_element(By.ID, 'ucCenarioFinanceiro2_txtQt_Area_Estabelecimento').send_keys(pj.areaEstabelecimento)
        driver.find_element(By.ID, 'ucCenarioFinanceiro2_txtQt_Area_Estabelecimento_Grupo').send_keys(pj.areaTotal)
        driver.find_element(By.ID, 'ucCenarioFinanceiro2_txtAreaConstruida').send_keys(pj.areaConstruida)
        time.sleep(1)
        print('Faturamento Anual: ', pj.faturamentoAnual)
        print('Faturamento Mensal: ', pj.faturamentoMensal)
        driver.find_element_by_id('ucCenarioFinanceiro2_txtVl_Faturamento_Grupo_Anual')\
            .send_keys(f'{pj.faturamentoAnual:.2f}')
        driver.find_element_by_id('ucCenarioFinanceiro2_txtVl_Faturamento_Grupo_Mensal')\
            .send_keys(f'{pj.faturamentoMensal:.2f}')

        photo.takeShot()

        time.sleep(2)
        driver.find_element(By.ID, 'rbInformarBensNao').click()
        time.sleep(1)
        driver.find_element(By.ID, 'txtNovoMotivo').send_keys(pj.pfJustificativa)

        photo.takeShot()

    def fim():
        driver.find_element(By.ID, 'menuFluxo').click()
        time.sleep(1)
        tipoFila = Select(driver.find_element(By.ID, 'ddlTipoFluxo'))
        tipoFila.select_by_value('8')
        driver.find_element(By.ID, 'txtFluxoObservacao').send_keys(pj.parecer + nv)
        time.sleep(1)

        photo.takeShot()

    if nv == '1':
        nv1()
        fim()
        log.salva()
    elif nv == '2':
        nv1()
        nv2()
        fim()
        log.salva()
    elif nv == '3':
        nv1()
        nv2()
        nv3()
        fim()
        log.salva()
