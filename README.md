# Coletor de dados de parceiros Meliuz - Desafio Desenvolvedor FullStack

## Funcionalidades

Desafio resolvido utilizando a linguagem Python, com a biblioteca BeautifulSoup para fazer o parse do HTML e Requests para realizar as requisições HTTP.


## Dependências

- BeautifulSoup
- Requests


## Instalação das dependências

- No terminal execute os comandos abaixo:

pip install beautifulsoup4

pip install requests


# Arquivos disponíveis

- lista_parceiros.py

Responsável por coletar e extrair a lista de parceiros, que serão utilizados posteriormente pelo coletor_parceiros.py

Funções disponíveis:

obter_dados_parceiros -> Coleta os dados de todos os parceiros disponíveis na página de descontos da Méliuz
obter_parceiro_especifico -> Coleta os dados de um parceiro específico, recebendo como parâmetro o nome do parceiro.

- coletor_parceiros.py 

Esse script recebe como entrada um o código do parceiro, e extrai os detalhes necessários.


## Como rodar localmente

- No terminal execute os comandos abaixo para obter a lista de todos os parceiros e dados dos mesmos:

python lista_parceiros.py obter_parceiros

- Para obter os dados de um parceiro específico, execute o comando abaixo, passando o nome do parceiro como parâmetro, Exemplo:

python lista_parceiros.py obter_parceiro_especifico HP


## Criar uma imagem docker

- Para criar a imagem Docker, execute o comando:

docker build -t nome_da_imagem .

- Para rodar a imagem e obter a lista de parceiros:

docker run nome_da_imagem obter_parceiros

- Para rodar a imagem e obter dados de um parceiro específico:

docker run nome_da_imagem obter_parceiro_especifico HP


## Comportamento logado e deslogado

Ambos os casos de logado e deslogado no sistema apresentaram os dados corretamente dentro das páginas. Somente em alguns casos, como o parceiro Acer, foi observado que alguns cupons desaparecem após o login, provavelmente devido a alguma regra do tipo "apenas na primeira compra".



 
