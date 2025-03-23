import requests
from bs4 import BeautifulSoup

def coletar_cupons(parceiro):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    url = parceiro['link']
    nome = parceiro['nome']
    parceiro_info = {}
    cupons = []

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
      
    parceiro = soup.find('div', class_='hero-sec')

    if parceiro:
        url_imagem = parceiro.find('img')['src'] if parceiro.find('img') else ""

        parceiro_info['nome'] = nome
        parceiro_info['url_imagem'] = url_imagem
    
    # Pegar o cashback do botão, caso exista

    redirect_btn = soup.find("div", class_="redirect-btn")
    cashback_total = ""

    if redirect_btn:
        btn = redirect_btn.find("button", class_="a-red-btn")
        if btn:
            cashback_span = btn.find("span")
            if cashback_span:
                    cashback_total = cashback_span.text.strip()
            
    parceiro_info['cashback_total'] = cashback_total

    # Pegar os cupons disponíveis

    secao_cupons_disponiveis = soup.find_all('div', class_='cpn-layout offer-cpn')
    
    for item in secao_cupons_disponiveis:
        cupom = item.get("data-offer-code")
        url = item.get("data-offer-url")

        cashback = item.find('p', class_='offer-cpn__cashback')

        cashback = cashback.text.strip() if cashback else ""

        cashback_text_split = cashback.split(". era")

        cashback = cashback_text_split[0].strip() if len(cashback_text_split) > 0 else ""
        cashback_antigo =  cashback_text_split[1].strip() if len(cashback_text_split) > 1 else ""
            
        cashback = cashback.split(" ")[1] if cashback else ""
            
        cupons.append({
            "codigo": cupom if cupom else "",
            "status": "Disponível",
            "url": url,
            "cashback": cashback,
            "cashback_antigo": cashback_antigo
        })
        
    # Pegar os cupons expirados

    secao_cupons_expirados = soup.find('section', class_='expired-cpn-sec')

    if secao_cupons_expirados:
        for item in secao_cupons_expirados.find_all('li'):
            cupom = item.find('span', class_='expired-cpn-sec__code').text.strip()
            cupom_url = item['data-offer-url']
                
        cupons.append({
            "codigo": cupom if cupom else "",
            "status": "Expirado",
            "url": cupom_url
        })

    parceiro_info['cupons'] = cupons 

    return parceiro_info

 