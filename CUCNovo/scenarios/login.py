from selenium import webdriver

url = 'https://user_inmetrics09:Intruder*800@trbnethml.tribanco.com.br/Tribanco.CUC.WebUI/Default.aspx'
driver = webdriver.Chrome('../utils/chromedriver.exe')
driver.implicitly_wait(45)


def login():
    driver.maximize_window()
    driver.get(url)
