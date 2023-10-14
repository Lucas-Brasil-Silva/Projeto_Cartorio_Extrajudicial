import csv

class cnsFilter():
    """
    Classe para filtrar Códigos Nacionais de Serventia (CNS) a partir de um arquivo CSV.

    Esta classe fornece métodos para filtrar CNS com base em critérios como estado, município ou geral.
    O arquivo CSV deve seguir o formato CNS, Município, UF.

    Métodos:
        - geral(): Retorna uma lista de todos os CNS disponíveis.
        - municipio(municipio): Retorna uma lista de CNS com base no município especificado.
        - estado(estado): Retorna uma lista de CNS com base no estado especificado.
        - nomes_municipios(estado): Retorna uma lista de municípios disponíveis em um estado.

    Exemplo de Uso:

    >>> filtro = cnsFilter()
    >>> todos_cns = filtro.geral()
    >>> cns_por_municipio = filtro.municipio("SAO PAULO")
    >>> cns_por_estado = filtro.estado("SP")
    >>> municipios_em_sp = filtro.nomes_municipios("SP")
    """

    def __init__(self):
        pass

    @staticmethod
    def geral():
        """
        Retorna uma lista de todos os CNS disponíveis.

        Returns:
            list: Uma lista de CNS.
        """
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [cns for cns,municipio,uf in dados]
    
    @staticmethod
    def municipio(municipio):
        """
        Retorna uma lista de CNS com base no município especificado.

        Args:
            municipio (str): O nome do município a ser filtrado.

        Returns:
            list: Uma lista de CNS que pertencem ao município especificado.
        """
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [cns for cns,cidade,uf in dados if cidade in municipio]
    
    @staticmethod
    def estado(estado):
        """
        Retorna uma lista de CNS com base no estado especificado.

        Args:
            estado (str): A sigla do estado a ser filtrado.

        Returns:
            list: Uma lista de CNS que pertencem ao estado especificado.
        """
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [cns for cns,municipio,uf in dados if uf in estado]
    
    @staticmethod
    def nomes_municipios(estado):
        """
        Retorna uma lista de municípios disponíveis em um estado.

        Args:
            estado (str): A sigla do estado para listar municípios.

        Returns:
            list: Uma lista de municípios no estado especificado.
        """
        with open('codigo-indentificador.csv','r',encoding='UTF-8') as arquivo:
            dados = csv.reader(arquivo)
            return [municipio for cns,municipio,uf in dados if uf in estado]