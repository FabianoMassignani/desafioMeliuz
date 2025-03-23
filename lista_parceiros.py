import sys
import requests
from bs4 import BeautifulSoup
from coletor_parceiro import coletar_cupons
import json

def obter_dados_parceiros(parceiros):
    retorno = []
    for parceiro in parceiros:
        retorno.append(coletar_cupons(parceiro))

    with open('dados_parceiros.json', 'w', encoding='utf-8') as f:
        json.dump(retorno, f, ensure_ascii=False, indent=4)


def ober_dados_parceiro_especifico(parceiros, nome_parceiro):
    for parceiro in parceiros:
        if parceiro['nome'] == nome_parceiro:
            dados_parceiro = coletar_cupons(parceiro)

            with open('dados_parceiro_especifico.json', 'w', encoding='utf-8') as f:
                json.dump(dados_parceiro, f, ensure_ascii=False, indent=4)
            break       


def main():
    if len(sys.argv) < 2:
        print("Por favor, forneça a função a ser executada: 'obter_parceiros' ou 'obter_parceiro_especifico'.")
        return

    funcao = sys.argv[1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    page = requests.get('https://www.meliuz.com.br/desconto', headers=headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    # Encontra todos os parceiros da página
    grupos = soup.find_all('div', class_='partner-index-pg__partners-sec__group')

    parceiros = []

    for grupo in grupos:
        links_parceiros = grupo.find_all('a')

        for parceiro in links_parceiros:
            nome = parceiro.get_text(strip=True)
            link = 'https://www.meliuz.com.br' + parceiro.get('href')

            parceiros.append({"nome": nome, "link": link})

    with open('parceiros.json', 'w', encoding='utf-8') as f:
        json.dump({"parceiros": parceiros}, f, ensure_ascii=False, indent=4)

    if funcao == "obter_parceiros":
        obter_dados_parceiros(parceiros)
    
    if funcao == "obter_parceiro_especifico":
        if len(sys.argv) < 3:
            print("Por favor, forneça o nome do parceiro para a função 'obter_parceiro_especifico'.")
            return
        
        nome_parceiro = sys.argv[2]

        ober_dados_parceiro_especifico(parceiros, nome_parceiro)
    else:
        print(f"Função '{funcao}' não reconhecida.")

if __name__ == "__main__":
    main()


 