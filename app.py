import PySimpleGUI as sg
from cns_filter import cnsFilter
from dados_cartorio import main

sg.theme('Reddit')

def pagina_inicial():
    layout = [
        [sg.Text('Para gerar um arquivo excel escolha alguma das opções abaixo:')],
        [sg.Button('Todos os cartorios', key='geral')],
        [sg.Button('Por estado', key='estado')],
        [sg.Button('Por municipio', key='municipio')]
    ]

    return sg.Window(layout=layout, title='Pagina Inicial')

def geral_cartorios():
    layout = [
        [sg.Text('Digite o nome do arquivo excel:')],
        [sg.Input(key='panilha-geral')],
        [sg.Text('Clique no botão abaixo para iniciar:')],
        [sg.Button('Iniciar')]
    ]

    return sg.Window(layout=layout, title='Cartorios')

def cartorios_estado():
    layout = [
        [sg.Text('Escolha os estados:')],
        [sg.Checkbox('Amazonas', key='AM'), sg.Checkbox('Acre', key='AC')],
        [sg.Checkbox('Amapá', key='AP'), sg.Checkbox('Alagoas', key='AL')],
        [sg.Checkbox('Bahia', key='BA'), sg.Checkbox('Ceará', key='CE')],
        [sg.Checkbox('Distrito Federal', key='DF'), sg.Checkbox('Espírito Santo', key='ES')],
        [sg.Checkbox('Goiás', key='GO'), sg.Checkbox('Minas Gerais', key='MG')],
        [sg.Checkbox('Maranhão', key='MA'), sg.Checkbox('Mato Grosso do Sul', key='MS')],
        [sg.Checkbox('Mato Grosso', key='MT'), sg.Checkbox('Paraná', key='PR')],
        [sg.Checkbox('Pernambuco', key='PE'), sg.Checkbox('Paraíba', key='PB')],
        [sg.Checkbox('Piauí', key='PI'), sg.Checkbox('Pará', key='PA')],
        [sg.Checkbox('Rio Grande do Sul', key='RS'), sg.Checkbox('Rio Grande do Norte', key='RN')],
        [sg.Checkbox('Rondônia', key='RO'), sg.Checkbox('Roraima', key='RR')],
        [sg.Checkbox('Rio de Janeiro', key='RJ'), sg.Checkbox('Santa Catarina', key='SC')],
        [sg.Checkbox('Sergipe', key='SE'), sg.Checkbox('São Paulo', key='SP')],
        [sg.Checkbox('Tocantins', key='TO')],
        [sg.Text('Digite o nome do arquivo excel:')],
        [sg.Input(key='panilha-estado')],
        [sg.Button('Iniciar')]
    ]

    return sg.Window(layout=layout, title='Cartorios Estado')

def municipio_estado():
    layout = [
        [sg.Text('Escolha os estados:')],
        [sg.Checkbox('Amazonas', key='AM'), sg.Checkbox('Acre', key='AC')],
        [sg.Checkbox('Amapá', key='AP'), sg.Checkbox('Alagoas', key='AL')],
        [sg.Checkbox('Bahia', key='BA'), sg.Checkbox('Ceará', key='CE')],
        [sg.Checkbox('Distrito Federal', key='DF'), sg.Checkbox('Espírito Santo', key='ES')],
        [sg.Checkbox('Goiás', key='GO'), sg.Checkbox('Minas Gerais', key='MG')],
        [sg.Checkbox('Maranhão', key='MA'), sg.Checkbox('Mato Grosso do Sul', key='MS')],
        [sg.Checkbox('Mato Grosso', key='MT'), sg.Checkbox('Paraná', key='PR')],
        [sg.Checkbox('Pernambuco', key='PE'), sg.Checkbox('Paraíba', key='PB')],
        [sg.Checkbox('Piauí', key='PI'), sg.Checkbox('Pará', key='PA')],
        [sg.Checkbox('Rio Grande do Sul', key='RS'), sg.Checkbox('Rio Grande do Norte', key='RN')],
        [sg.Checkbox('Rondônia', key='RO'), sg.Checkbox('Roraima', key='RR')],
        [sg.Checkbox('Rio de Janeiro', key='RJ'), sg.Checkbox('Santa Catarina', key='SC')],
        [sg.Checkbox('Sergipe', key='SE'), sg.Checkbox('São Paulo', key='SP')],
        [sg.Checkbox('Tocantins', key='TO')],
        [sg.Button('Continuar')]
    ]

    return sg.Window(layout=layout, title='Cartorios Municipio')

def cartorios_municipio(lista):
    layout = [
        [sg.Text('Selecione os municipios dejesados:')],
        [sg.ScrollView(layout=[
            [sg.Checkbox(opcao, key=opcao) for opcao in lista]
        ], size=(300,150), scroll_x=True, scroll_y=True, key='scroll')]
        [sg.Text('Digite o nome da arquivo excel:')],
        [sg.Input(key='panilha-geral')],
        [sg.Button('Iniciar')]
    ]

    return sg.Window(layout=layout, title='Cartorios')

pagina_inicial_, geral_cartorios_, cartorios_estado_, municipio_estado_, cartorios_minicipio_ = pagina_inicial(), None, None, None, None

