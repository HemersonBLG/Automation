import os
import time

dirName = '../screenshot/' + time.strftime("%d_%m_%Y")


class TiraFoto(object):
    def __init__(self, driver=None, class_name='ClassName', cont=0, new_folder=0):
        self._driver = driver
        self._class_name = class_name
        self._cont = cont
        self._newFolder = new_folder

    def criaDiretorio(self):
        try:
            os.mkdir(dirName)
            print('\033[36m' + 'Diretorio ' + dirName + ' criado\033[0;0m')
        except FileExistsError:
            print('\033[31m' + 'Diretorio ' + dirName + ' já existente\033[0;0m')

    def criaSubpasta(self):
        # variavel deve ser declarada aqui para atualizar o valor dela
        self._dirConta = dirName + '/' + str(self._newFolder) + '/'
        try:
            os.mkdir(self._dirConta)
            print('\033[36m' + 'Diretorio ' + self._dirConta + ' criado\033[0;0m')
            return self
        except FileExistsError:
            self._newFolder = self._newFolder + 1
            print('\033[31m' + 'Diretorio ' + self._dirConta + ' já existente\033[0;0m')
            return False

    def tira_foto(self):
        # file_name = time.strftime("%d_%m_%Y_%H_%M_%S") + '-' + self._class_name + ' (' + str(self._cont) + ')'
        file_name = self._class_name + ' (' + str(self._cont) + ')'
        dirName = self._dirConta
        self._driver.save_screenshot(dirName + file_name + '.png')
        self._cont += 1
        return self
