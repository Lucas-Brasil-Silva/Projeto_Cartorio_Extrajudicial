"""
Programa para Extração de Dados de Cartórios com Interface Gráfica usando PySimpleGUI
=====================================================================================

Este programa foi desenvolvido para facilitar a extração de dados de cartórios a partir do site do CNJ (Conselho Nacional de Justiça). Ele oferece uma interface gráfica simples que permite ao usuário selecionar os critérios de extração, como estado, município ou todos os cartórios, e fornece a capacidade de salvar os dados em um arquivo Excel.

Requisitos
----------
- Python 3.x
- Biblioteca PySimpleGUI (instalável com 'pip install PySimpleGUI')
- Outras bibliotecas, como 'cns_filter' e 'dados_cartorio', que devem estar disponíveis no sistema

Instruções de Uso
----------------
1. Certifique-se de que o Python e as bibliotecas necessárias estejam instalados.
2. Execute o programa.
3. Escolha uma das opções disponíveis na tela inicial: Por estado, Por município ou Todos os cartórios.
4. Siga as instruções na interface gráfica para configurar e iniciar o processo de extração de dados.

Funções e Janelas
-----------------
- **pagina_inicial()**: Apresenta a tela inicial do programa com opções para escolher o tipo de extração.
- **geral_cartorios()**: Permite ao usuário extrair dados de todos os cartórios e especificar o nome do arquivo Excel.
- **cartorios_estado()**: Permite ao usuário escolher estados para extrair dados e especificar o nome do arquivo Excel.
- **municipio_estado()**: Permite ao usuário escolher estados para extrair dados de municípios e continuar para a próxima etapa.
- **cartorios_municipio(lista_municipio)**: Permite ao usuário selecionar municípios para extrair dados e especificar o nome do arquivo Excel.
- **output()**: Apresenta informações sobre o processo de extração e permite ao usuário continuar ou finalizar o programa.

- **main()**: Função principal que inicia a interface gráfica, controla as transições entre as janelas e inicia a extração de dados quando apropriado.

Autor
-----
Nome: Lucas Brasil Silva
Email: lucasbrasil396@gmail.com
----
Última atualização: 14/10/2023

"""

import PySimpleGUI as sg
from cns_filter import cnsFilter
from dados_cartorio import cartorios
from threading import Thread

sg.theme('Reddit')
sg.set_options(font=('',11))

def pagina_inicial():
    layout = [
        [sg.Text('Para gerar um arquivo excel referente a dados de um cartório x, escolha alguma das opções abaixo:', size=(46,2))],
        [sg.Button('Por estado', key='estado')],
        [sg.Button('Por município', key='municipio')],
        [sg.Button('Todos os cartórios', key='geral')]
    ]

    return sg.Window(layout=layout, title='Pagina Inicial', finalize=True)

def geral_cartorios():
    layout = [
        [sg.Text('Digite o nome do arquivo excel:')],
        [sg.Input(key='panilha-geral')],
        [sg.Text('Clique no botão iniciar:')],
        [sg.Button('Iniciar', key='iniciar'), sg.Button('Voltar', key='voltar')]
    ]

    return sg.Window(layout=layout, title='Cartórios', finalize=True)

def cartorios_estado():
    lista_sigla = ['AM','AC','AP','AL','BA','CE','DF','ES','GO','MG','MA','MS','MT','PR','PE','PB','PI','PA','RS','RN','RO','RR','RJ','SC','SE','SP','TO']
    lista_estencao = ['Amazonas','Acre','Amapá','Alagoas','Bahia', 'Ceará','Distrito Federal','Espírito Santo','Goiás','Minas Gerais','Maranhão','Mato Grosso do Sul','Mato Grosso','Paraná','Pernambuco','Paraíba','Piauí','Pará','Rio Grande do Sul','Rio Grande do Norte','Rondônia','Roraima','Rio de Janeiro','Santa Catarina','Sergipe','São Paulo','Tocantins']
    layout = [
        [sg.Text('Escolha os estados:')],
        [sg.Column([
            [sg.Checkbox(estado, font=('Arial',12), key=sigla)] for estado,sigla in zip(lista_estencao,lista_sigla)], scrollable=True, vertical_scroll_only=True, size=(350,200),key='column')],
        [sg.Text('Digite o nome do arquivo excel:')],
        [sg.Input(key='panilha-estado')],
        [sg.Button('Iniciar', key='iniciar'), sg.Button('Voltar', key='voltar')]
    ]

    return sg.Window(layout=layout, title='Cartórios Estado', finalize=True)

def municipio_estado():
    lista_sigla = ['AM','AC','AP','AL','BA','CE','DF','ES','GO','MG','MA','MS','MT','PR','PE','PB','PI','PA','RS','RN','RO','RR','RJ','SC','SE','SP','TO']
    lista_estencao = ['Amazonas','Acre','Amapá','Alagoas','Bahia', 'Ceará','Distrito Federal','Espírito Santo','Goiás','Minas Gerais','Maranhão','Mato Grosso do Sul','Mato Grosso','Paraná','Pernambuco','Paraíba','Piauí','Pará','Rio Grande do Sul','Rio Grande do Norte','Rondônia','Roraima','Rio de Janeiro','Santa Catarina','Sergipe','São Paulo','Tocantins']
    layout = [
        [sg.Text('Escolha os estados:')],
        [sg.Column([
            [sg.Checkbox(estado, font=('Arial',12), key=sigla)] for estado,sigla in zip(lista_estencao,lista_sigla)], scrollable=True, vertical_scroll_only=True, size=(300,200),key='column')],
        [sg.Button('Continuar', key='continuar'), sg.Button('Voltar', key='voltar')]
    ]

    return sg.Window(layout=layout, title='Cartórios Município', finalize=True)

def cartorios_municipio(lista_municipio):
    layout = [
        [sg.Text('Selecione os municípios desejados:')],
        [sg.Listbox(values=lista_municipio, select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(45,15), key='opcoes')],
        [sg.Text('Digite o nome da arquivo excel:')],
        [sg.Input(key='panilha-municipio')],
        [sg.Button('Iniciar', key='iniciar'), sg.Button('Voltar', key='voltar')]
    ]

    return sg.Window(layout=layout, title='Cartórios Município', finalize=True)

def output():
    layout = [
        [sg.Text('Informações do processo de extração dos dados:')],
        [sg.Output(size=(40,10))],
        [sg.Button('Continuar', key='continuar'), sg.Button('Finalizar', button_color='red')]
    ]

    return sg.Window(layout=layout, title='Processos', finalize=True)

def main():
    pagina_inicial_, geral_cartorios_, cartorios_estado_, municipio_estado_, cartorios_minicipio_, output_ = pagina_inicial(), None, None, None, None, None

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WINDOW_CLOSED:
            break

        elif window == pagina_inicial_:
            if event == 'estado':
                pagina_inicial_.hide()
                cartorios_estado_ = cartorios_estado()

            elif event == 'municipio':
                pagina_inicial_.hide()
                municipio_estado_ = municipio_estado()

            elif event == 'geral':
                pagina_inicial_.hide()
                texto = open('aviso.txt',encoding='UTF-8').read()
                sg.popup_scrolled(texto, title='Importante', font=('Arial', 14), size=(45,10))
                geral_cartorios_ = geral_cartorios()

        elif window == geral_cartorios_:
            if event == 'iniciar':
                if values['panilha-geral']:
                    lista = cnsFilter.geral()
                    planilha = values['panilha-geral']
                    funcao = Thread(target=cartorios, args=(lista,planilha),daemon=True)
                    funcao.start()
                    sg.popup_ok('Espere a extração dos dados finalizar, não inicie outra!!', title='Aviso')
                    cartorios_estado_.close()
                    output_ = output()
                else:
                    sg.popup_error('Por favor, Digitar um nome para o arquivo Excel', title='Nome Arquivo')
            elif event == 'voltar':
                geral_cartorios_.close()
                pagina_inicial_.un_hide()
        
        elif window == cartorios_estado_:
            if event == 'iniciar':
                if values['panilha-estado']:
                    estados = [key for key,value in values.items() if value == True]
                    if estados:
                        lista = cnsFilter.estado(estados)
                        planilha = values['panilha-estado']
                        funcao = Thread(target=cartorios, args=(lista,planilha),daemon=True)
                        funcao.start()
                        sg.popup_ok('Espere a extração dos dados finalizar, não inicie outra!!', title='Aviso')
                        cartorios_estado_.close()
                        output_ = output()
                    else:
                        sg.popup_error('Por favor, Escolha um ou mais estados:', title='Estados')    
                else:
                    sg.popup_error('Por favor, Digitar um nome para o arquivo Excel', title='Nome Arquivo')
            elif event == 'voltar':
                cartorios_estado_.close()
                pagina_inicial_.un_hide()

        elif window == municipio_estado_:
            if event == 'continuar':
                estados = [key for key,value in values.items() if value == True]
                if estados:
                    municipio_estado_.hide()
                    lista_municipio = cnsFilter.nomes_municipios(estados)
                    cartorios_minicipio_ = cartorios_municipio(lista_municipio)
                else:
                    sg.popup_error('Por favor, Escolha um ou mais estados:', title='Estados')

            elif event == 'voltar':
                municipio_estado_.close()
                pagina_inicial_.un_hide()

        elif window == cartorios_minicipio_:
            municipio_estado_.close()
            if event == 'iniciar':
                if values['panilha-municipio']:
                    municipios = values['opcoes']
                    if municipios:
                        lista = cnsFilter.municipio(municipios)
                        planilha = values['panilha-municipio']
                        sg.popup_ok('Espere a extração dos dados finalizar, não inicie outra!!', title='Aviso')
                        funcao = Thread(target=cartorios,args=(lista,planilha),daemon=True)
                        funcao.start()
                        cartorios_minicipio_.close()
                        output_ = output()
                    else:
                        sg.popup_error('Por favor, Escolha um ou mais municipios:', title='Municipios')    
                else:
                    sg.popup_error('Por favor, Digitar um nome para o arquivo Excel', title='Nome Arquivo')
            elif event == 'voltar':
                cartorios_minicipio_.close()
                pagina_inicial_.un_hide()

        elif window == output_:
            if event == 'continuar':
                output_.close()
                pagina_inicial_.un_hide()
            else:
                break

if __name__ == '__main__':
    main()