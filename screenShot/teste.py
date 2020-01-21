import pyscreenshot as ImageGrab
import time


def main():
    i = 0
    for i in range (3):
        time.sleep(5)
        imagem = ImageGrab.grab()
        imagem.save('tes' + str(i) + '.jpg', 'jpeg')


main()
