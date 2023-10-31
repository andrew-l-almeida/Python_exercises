import requests
from bs4 import BeautifulSoup

# Função para pesquisar a palavra-chave em um site específico
def search_keyword_on_site(keyword, site_url):
    # Construa a URL da pesquisa
    search_url = f"{site_url}/?s={keyword}"

    # Faça uma solicitação HTTP para a página de pesquisa
    response = requests.get(search_url)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analise o HTML da página de pesquisa
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontre os links dos resultados da pesquisa
        result_links = soup.select('div.post-inner header.entry-header h2.entry-title')

        if result_links:
            # Obtenha o primeiro link dos resultados (ou personalize a seleção)
            for i,link in  enumerate(result_links, start=1):
                print(f'{i}: {link.a.get_text()} -> {link.a["href"]}')
                print('-' * len(link.a.get_text())*2)
                print()

            # Construa a URL completa do resultado

            return True

    return None

# Exemplo de uso
keyword = input('Digite a pesquisa: ')  # Sua palavra-chave
print()
site_url = "https://vestibulares.estrategia.com/portal"  # URL do site específico (substitua com o site real)

result = search_keyword_on_site(keyword, site_url)  

# if result:
#     print(f"Link para a página relacionada: {result}")
# else:
#     print("Nenhum resultado encontrado.")


"""
Meu primeiro trabalho foi como aprendiz de eletricista, na empresa Teadit, estudando elétrica no Senai. 
Quando conheci a programação e as oportunidades que ela oferece, iniciei o curso de Análise e desenvolvimento de sistemas. Nesse período já estava em uma nova empresa (Plastiveda) do ramo de juntas de vedações. 
Fui contrato como auxiliar de qualidade, mas otimizei os processos do meu trabalho por meio da programação. Devido a isso, atualmente trabalho para implantar e desenvolver melhorias no estoque e no sistema da fábrica.


My first job was as a apprentice eletrician while I was studying at Senai. When I discovered programming

"""