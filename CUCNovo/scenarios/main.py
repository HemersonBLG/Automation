from scenarios import login
from scenarios import cadastro
from scenarios import cadastroPJ
import time

escolha = input('Selecione uma das duas opções:\n'
                '1 - PF\n'
                '2 - PJ\n')
login.login()
time.sleep(3)
if escolha == '1':
    cadastro.cadPF()
    cadastro.insereDadosPessoa()
elif escolha == '2':
    cadastroPJ.cadPJ()
    cadastroPJ.insereDados()
print('Dados inseridos, aguardando envio para aprovação.')
