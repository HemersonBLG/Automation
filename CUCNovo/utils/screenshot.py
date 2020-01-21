import os
import time
from PIL import ImageGrab

dir_name = '../screenshot/' + time.strftime('%d_%m_%Y')


class TakeShoot(object):
    def __init__(self, driver=None, class_name='ClassName', cont=0, new_folder=0, count=0):
        self._driver = driver
        self._class_name = class_name
        self._cont = cont
        self._newFolder = new_folder
        self._dirCount = count

    def createDiretory(self):
        try:
            os.mkdir(dir_name)
            print('\033[36m' + 'Diretorio ' + dir_name + ' criado\033[0;0m')
        except FileExistsError:
            print('\033[31m' + 'Diretorio ' + dir_name + ' já existente\033[0;0m')

    def createSubPaste(self):
        self._dirCount = dir_name + '/' + str(self._newFolder) + '/'
        try:
            os.mkdir(self._dirCount)
            print('\033[36m' + 'Diretorio ' + self._dirCount + ' criado\033[0;0m')
            return self
        except FileExistsError:
            self._newFolder = self._newFolder + 1
            print('\033[31m' + 'Diretorio ' + self._dirCount + ' já existente\033[0;0m')
            return False

    def takeShot(self):
        file_name = str(self._dirCount) + self._class_name + '_' + str(self._cont) + '.png'
        print(file_name)
        ImageGrab.grab().save(file_name)
        self._cont += 1
        return self
