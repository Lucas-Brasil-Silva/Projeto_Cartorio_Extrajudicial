# Projeto_Cartorio_Extrajudicial
<p align="justify">Este é um programa Python com interface gráfica desenvolvida com PySimpleGUI para automatizar a extração de informações de cartórios do site do Conselho Nacional de Justiça (CNJ). Ele permite que o usuário escolha critérios de extração, como estados, municípios ou todos os cartórios, e exporta os dados para um arquivo Excel.</p>

## 🛠️ Tecnologias Utilizadas
Principais tecnologias usadas:
Selenuim - PysimpleGUI - openpyxl

## 📌 Status do Projeto
 
✅ *Projeto concluído*  ✅ 

## Licença
Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## 🔧 Instruções de Uso

### 📋 Instalação Das Dependências
Para instalar as dependências do projeto, execute o seguinte comando:
```bash
pip install -r requirements.txt
```
### ⚙️ Iniciando a Aplicação
Para iniciar a aplicação de extração de informações de cartórios, execute o seguinte comando:
```bash
python app.py
```
## 🚀 Instruções de uso
#### Página Inicial
Apresenta a tela inicial do programa com opções para escolher o tipo de extração:

![Página inicial](imagens/pagina-inicial.JPG)

#### Página Geral Cartórios
Permite ao usuário extrair dados de todos os cartórios e especificar o nome do arquivo Excel.

![Página Geral Cartórios 1](imagens/pagina-geral-1.JPG)

![Página Geral Cartórios 2](imagens/pagina-geral-2.JPG)

#### Página Cartórios Estado
Permite ao usuário escolher estados para extrair dados e especificar o nome do arquivo Excel.

![Página Cartórios Estado](imagens/pagina-estado.JPG)

#### Página Cartórios Município
Permite ao usuário escolher estados para extrair dados de municípios e continuar para a próxima etapa.

![Página Cartórios Município 1](imagens/pagina-municipio-1.JPG)

Permite ao usuário selecionar municípios para extrair dados e especificar o nome do arquivo Excel.

![Página Cartórios Município 2](imagens/pagina-municipio-2.JPG)

#### Página Processos
Apresenta informações sobre o processo de extração e permite ao usuário continuar ou finalizar o programa.

![Página Processos](imagens/pagina-saida.JPG)

### 🚨 Tipos de Erros

**Quando o não é fornecido um nome para planilha:**

![imagem erro 1](imagens/tratamento-erro-1.JPG)

**Quando não é feita a escolha de um estado:**

![imagem erro 2](imagens/tratamento-erro-2.JPG)

**Quando não é feita a escolha de um município:**

![imagem erro 3](imagens/tratamento-erro-3.JPG)

**Aviso para que não seja executado mais de uma extração por vez:**

![imagem erro 4](imagens/tratamento-erro-4.JPG)

