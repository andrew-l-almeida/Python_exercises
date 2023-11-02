import requests
from bs4 import BeautifulSoup


def search_keyword_on_site(keyword, site_url):

    search_url = f"{site_url}/?s={keyword}"


    response = requests.get(search_url)


    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')


        result_links = soup.select('div.post-inner header.entry-header h2.entry-title')

        if result_links:

            for i,link in  enumerate(result_links, start=1):
                print(f'{i}: {link.a.get_text()} -> {link.a["href"]}')
                print('-' * len(link.a.get_text())*2)
                print()


            return True

    return None

keyword = input('Digite a pesquisa: ') 
print()
site_url = "https://vestibulares.estrategia.com/portal" 

result = search_keyword_on_site(keyword, site_url)  
