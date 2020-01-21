import time


class TiraFoto(object):
    def __init__(self, driver=None, class_name='ClassName'):
        self._driver = driver
        self._class_name = class_name

    def tira_foto(self):
        dir_path = "../screenshot/"
        file_name = time.strftime("%d_%m_%Y_%H_%M_%S") + '-' + self._class_name
        self._driver.save_screenshot(dir_path + file_name + '.png')
        return self
