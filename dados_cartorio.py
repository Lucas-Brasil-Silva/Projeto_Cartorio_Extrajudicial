"""
Programa de Web Scraping para Extrair Dados de Cartórios
===========================================

Este programa utiliza a biblioteca Selenium para automatizar a navegação em um site e extrair informações sobre cartórios. Ele foi projetado para funcionar com o site https://www.cnj.jus.br/corregedoria/justica_aberta/? e exportar os dados para um arquivo Excel.

Requisitos
----------
- Python 3.x
- Biblioteca Selenium (instalável com 'pip install selenium')
- Google Chrome instalado no sistema
- ChromeDriver instalado e configurado no sistema (https://sites.google.com/chromium.org/driver/)

Instruções
----------
1. Certifique-se de que o Python e as bibliotecas necessárias estejam instalados.
2. Certifique-se de que o ChromeDriver esteja configurado corretamente e disponível no PATH do sistema.
3. Execute o programa, fornecendo a lista de CNS (Código Nacional de Serventia) e o nome da planilha.

Exemplo de Uso
--------------
lista_cns = ['CNS1', 'CNS2', 'CNS3']
nome_planilha = 'dados_cartorios'
cartorios(lista_cns, nome_planilha)

Funções
-------
- iniciar_driver(): Inicializa o driver do Selenium e retorna uma instância do driver e um objeto de espera.
- planilha(): Cria uma nova planilha Excel para armazenar os dados.
- cartorios(lista_cns, nome_planilha): Inicia a extração de dados dos cartórios e salva as informações na planilha especificada.

Este programa é específico para o site https://www.cnj.jus.br/corregedoria/justica_aberta/ e pode precisar de ajustes se o site for modificado.

Autor
-----
Nome: Lucas Brasil Silva
Email: lucasbrasil396@gmail.com
----
Última atualização: 14/10/2023

"""

from selenium import webdriver
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.support.ui    import WebDriverWait
from selenium.common.exceptions   import *
from selenium.webdriver.support  import expected_conditions as CondicaoEsperada
from selenium.webdriver.common.by  import By
from time import sleep
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

def cartorios(lista_cns,nome_planilha):
    driver, wait = iniciar_driver()
    print('Abrindo o site desejado!!\n')
    driver.get('https://www.cnj.jus.br/corregedoria/justica_aberta/?')
    sleep(3)

    workbook, sheet = planilha()
    sheet.append(['NOME','RESPONSAVEL','ATRIBUICAO','TELEFONE','EMAIL','MUNICIPIO','UF'])
    print('Iniciando a extração dos respectivos dados do cartório!!\n')
    print(f'Total de páginas a serem varridas {len(lista_cns)}\n')
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
    print('Processo de extração dos dados finalizado com sucesso!!')
    driver.close()