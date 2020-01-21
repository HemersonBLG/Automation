from scenarios import login
from dados import cadastro
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.screenshot import TakeShoot
from utils.saveCPF import Grava
import time

driver = login.driver
pf = cadastro
photo = TakeShoot(driver,  'TESTE')
photo.createDiretory()
while not photo.createSubPaste():
    print('\033[32m' + 'Criando outra pasta')


def cadPF():
    driver.find_element(By.ID, 'btnCadastrar').click()
    photo.takeShot()
    driver.find_element(By.LINK_TEXT, 'PF').click()


def insereDadosPessoa():
    photo.takeShot()
    nv = input('\033[1;93m' + '\033[1;100m' + 'Qual o nível de preenchimento?' + '\033[0;0m\n')
    log = Grava('1', nv, pf.pfCPF)

    def nv1():
        time.sleep(3)
        driver.find_element(By.ID, 'ucPessoa1_txtCpfPF').click()
        driver.find_element(By.ID, 'ucPessoa1_txtCpfPF').send_keys(pf.pfCPF)
        driver.find_element(By.ID, 'ucPessoa1_txtNomePF').send_keys(pf.pfNome)

    def nv2():
        driver.find_element(By.ID, 'ucPessoa1_txtDataNascimentoPF').click()
        driver.find_element(By.ID, 'ucPessoa1_txtDataNascimentoPF').send_keys(pf.pfDtNscto)
        doc = Select(driver.find_element(By.ID, 'ddlTipoDocumentoPF'))
        doc.select_by_value('RG')
        driver.find_element(By.ID, 'ucPessoa1_txtNroRegistroPF').send_keys(pf.pfRG)
        driver.find_element(By.ID, 'ucPessoa1_txtOrgaoEmissorPF').send_keys(pf.pfOrgEmissor)
        driver.find_element(By.ID, 'ucPessoa1_txtDataExpedicaoPF').send_keys(pf.pfRGEmissao)
        driver.find_element(By.ID, 'ucPessoa1_rbSexoFemininoPF').click()
        driver.find_element(By.ID, 'ucPessoa1_txtNomeMaePF').send_keys(pf.pfNomeMae)

        uf = Select(driver.find_element(By.ID, 'ddlEstadoPF'))
        uf.select_by_value('10')

        cid = Select(driver.find_element(By.ID, 'ddlNaturalidadePF'))
        cid.select_by_value('1148')

        estCivil = Select(driver.find_element(By.ID, 'ddlEstadoCivilPF'))
        estCivil.select_by_value('1')
        time.sleep(1)
        photo.takeShot()

        nvEscolar = Select(driver.find_element(By.ID, 'ucPessoa1_ddlNivelEscolaridadePF'))
        nvEscolar.select_by_value('11')

        natOcupacao = Select(driver.find_element(By.ID, 'ucPessoa1_ddlNaturezaOcupacaoPF'))
        natOcupacao.select_by_value('1')

        grpOcupacao = Select(driver.find_element(By.ID, 'ucPessoa1_ddlGrupoOcupacaoPF'))
        grpOcupacao.select_by_value('21')

        ocupacao = Select(driver.find_element(By.ID, 'ucPessoa1_ddlProfissoesPF'))
        ocupacao.select_by_value('21000')

        time.sleep(1)
        photo.takeShot()

        driver.find_element(By.ID, 'ucEndereco1_txtCEPSede').send_keys(pf.pfCep)
        driver.find_element(By.ID, 'btnPesquisarCEPSede').click()
        driver.find_element(By.ID, 'ucEndereco1_txtNumeroSede').click()
        driver.find_element(By.ID, 'ucEndereco1_txtNumeroSede').send_keys(pf.pfNumCasa)
        driver.find_element(By.ID, 'rbEndInternacionalFalsePJ').click()
        time.sleep(1)
        photo.takeShot()

    def nv3():
        # Contact Include
        driver.find_element(By.CSS_SELECTOR, "[data-target='#addContato']").click()
        driver.find_element(By.ID, 'txtNomeCtto').send_keys(pf.contatoNome)
        relacao = Select(driver.find_element(By.ID, 'ddlRelacaoCargoCtto'))
        relacao.select_by_value('14')
        tipoContato = Select(driver.find_element(By.ID, 'ddlMeioComunicacaoCtto'))
        tipoContato.select_by_value('3')
        driver.find_element(By.ID, 'txtDescComunicacaoCtto').send_keys(pf.contatoTelefone)
        time.sleep(1)
        photo.takeShot()
        driver.find_element(By.ID, 'btnInserirContato').click()

        # Comertial Reference
        driver.find_element(By.CSS_SELECTOR, "[data-target='#addRefComercial']").click()
        driver.find_element(By.ID, 'txtRazaoSocialCom').send_keys(pf.empresaNome)
        driver.find_element(By.ID, 'txtTelefoneCom').send_keys(pf.empresaCel)
        photo.takeShot()
        driver.find_element(By.ID, 'btnInserirRefComercial').click()

        # Personal Reference
        driver.find_element(By.CSS_SELECTOR, "[data-target='#addRefPessoal']").click()
        driver.find_element(By.ID, 'txtNomeRefPessoal').send_keys(pf.contatoNome)
        driver.find_element(By.ID, 'txtTelefoneRefPessoal').send_keys(pf.contatoTelefone)
        photo.takeShot()
        driver.find_element(By.ID, 'btnInserirRefPessoal').click()
        # Confirmed Reference
        driver.find_element(By.ID, 'cbReferenciaConfirmada').click()
        photo.takeShot()
        time.sleep(2)
        driver.find_element(By.ID, 'rbInformarBensNao').click()
        time.sleep(1)
        driver.find_element(By.ID, 'txtNovoMotivo').send_keys(pf.pfJustificativa)
        photo.takeShot()

    def fim():
        driver.find_element(By.ID, 'menuFluxo').click()
        time.sleep(1)
        tipoFila = Select(driver.find_element(By.ID, 'ddlTipoFluxo'))
        tipoFila.select_by_value('8')
        driver.find_element(By.ID, 'txtFluxoObservacao').send_keys(pf.parecer + nv)
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
