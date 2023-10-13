from selenium import webdriver
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.support.ui    import WebDriverWait
from selenium.common.exceptions   import *
from selenium.webdriver.support  import expected_conditions as CondicaoEsperada
from selenium.webdriver.common.by  import By
from bs4 import BeautifulSoup
from time   import sleep
import openpyxl
from cns_filter import cnsFilter

def iniciar_driver():
    chromeoptions = Options()
    arguments = ['--lang=pt-BR', 'window-size=1000,800', '--incognito']
    for argument in arguments:
        chromeoptions.add_argument(argument)
    
    chromeoptions.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    chromeoptions.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(options=chromeoptions)

    wait = WebDriverWait(
        driver,
        timeout=60,
        poll_frequency=1,
        ignored_exceptions=[
            ElementNotVisibleException,
            ElementNotInteractableException,
            NoSuchElementException,
        ]
        )


    return driver, wait

def planilha():
    workbook = openpyxl.Workbook()
    workbook['Sheet'].title = 'Cartorios'
    sheet = workbook['Cartorios']
    return workbook, sheet

def main(lista_cns,nome_planilha):
    driver, wait = iniciar_driver()
    driver.get('https://www.cnj.jus.br/corregedoria/justica_aberta/?')
    sleep(3)

    workbook, sheet = planilha()
    sheet.append(['NOME','RESPONSAVEL','ATRIBUICAO','TELEFONE','EMAIL','MUNICIPIO','UF'])
    for cns in lista_cns:
        wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH, '//div[@class="menu_int"]//ul/li/a[@class="dropdown-toggle"]'))).click()

        wait.until(CondicaoEsperada.visibility_of_all_elements_located((By.XPATH, '//div[@class="menu_int"]//ul[@class="dropdown-menu"]//a')))[0].click()

        campo_cns = wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH, '//input[@id="COD_IDENTIFICACAO_UNICA"]')))
        campo_cns.send_keys(cns)

        wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        
        estado = wait.until(CondicaoEsperada.visibility_of_all_elements_located((By.XPATH, '//fieldset/legend/b')))

        cartorio = wait.until(CondicaoEsperada.visibility_of_all_elements_located((By.XPATH, '//table/tbody/tr/td[@align]')))
        
        nome = cartorio[2].text
        responsavel = cartorio[4].text
        atribuicoes = cartorio[6].text
        telefone = cartorio[10].text.split(' ')[0]
        email = cartorio[10].text.split(' ')[-1]
        cidade = estado[0].text
        uf = estado[1].text

        sheet.append([nome,responsavel,atribuicoes,telefone,email,cidade,uf])

    workbook.save(f'{nome_planilha}.xlsx')
    print('Processo Finalizado')

    driver.close()

if __name__ == '__main__':
    lista_cns = cnsFilter.municipio(['FLORIANOPOLIS'])
    main(lista_cns,'planilha-municipio')
