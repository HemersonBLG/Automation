import os
import time
from utils.screenshot import TakeShoot
dire = TakeShoot


class Grava(object):
    def __init__(self, escolha=None, nv=None, cadcod=None):
        self._escolha = escolha
        self._nv = nv
        self._cadCop = cadcod

    def salva(self):
        with open(os.path.abspath('log.txt'), 'r') as arquivo:
            conteudo = arquivo.readlines()
            if self._escolha == '1':
                conteudo.append(''
                                'Foi cadastrado o CPF: {}\nOnde possui nível: {}\n{}\n\n'
                                '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n\n'
                                .format(self._cadCop, self._nv, time.strftime('%d-%m-%Y, %H:%M:%S')))
            elif self._escolha == '2':
                conteudo.append(''
                                'Foi cadastrado o CNPJ: {}\nOnde possui nível: {}\n{}\n\n'
                                '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n\n'
                                .format(self._cadCop, self._nv, time.strftime('%d-%m-%Y, %H:%M:%S')))
            arquivo = open('log.txt', 'w')
            arquivo.writelines(conteudo)


'''
arquivo = open('nome.txt', 'r') # Abra o arquivo (leitura)
conteudo = arquivo.readlines()
conteudo.append('Nova linha')   # insira seu conteúdo

arquivo = open('nome.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

arquivo.close()
'''