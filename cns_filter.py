import csv

class cnsFilter():
    
    @staticmethod
    def geral():
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [cns for cns,municipio,uf in dados]
    
    @staticmethod
    def municipio(municipio):
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [cns for cns,cidade,uf in dados if cidade in municipio]
    
    @staticmethod
    def estado(estado):
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [cns for cns,municipio,uf in dados if uf in estado]