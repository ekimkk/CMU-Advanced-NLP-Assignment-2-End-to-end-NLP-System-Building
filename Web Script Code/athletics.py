import requests 
from bs4 import BeautifulSoup 
import time 

urls1 = ["https://athletics.cmu.edu/athletics/mascot/about"]
urls = ["https://athletics.cmu.edu/athletics/tartanfacts/", "https://athletics.cmu.edu/athletics/mascot/about", "https://athletics.cmu.edu/athletics/kiltieband/index"]
remove_list = ["Search", "CMU on Instagram", "CMU on Facebook", "CMU on Twitter", "Search this site only", "© 2024 Carnegie Mellon University"]
# proxy_addresses = {
#     'http': 'http://72.206.181.123:4145',
#     'https': 'http://191.96.100.33:3128'
# }
request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
def scrape_word(urls): 
    out = []
    for url in urls:
        response = requests.get(url, headers=request_headers)#, proxies=proxy_addresses)
        print(response.status_code)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        words = str(soup.get_text()).strip()
        sentences = [i.strip() for i in words.split("\n")]
        sentences = [i for i in sentences if len(i) != 0]
        sentences = list(filter(lambda x: x not in remove_list, sentences))
        hrefs = []
        for a in soup.find_all('a', href=True):
            if "html" in a['href']:
                print(a['href'])
                hrefs.append(a['href'])
        hrefs = list(set(hrefs))
        # for i in hrefs:
        #     response = requests.get(url+i, timeout=5)
        #     soup = BeautifulSoup(response.content, 'html.parser')
        #     words = str(soup.get_text()).strip()
        #     s = [i.strip() for i in words.split("\n")]
        #     s = [i for i in s if len(i) != 0]
        #     sentences.extend(s)
        out.extend(sentences)

    with open('athletics.txt', 'w') as f:
        for i in out:
            f.write(i)
            f.write("\n")

scrape_word(urls)
