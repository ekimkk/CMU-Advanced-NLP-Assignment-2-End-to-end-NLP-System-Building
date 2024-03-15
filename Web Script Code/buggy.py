import requests 
from bs4 import BeautifulSoup 
import time 

results = {}
# urls = ["https://www.cs.cmu.edu/scs25/25things","https://www.cs.cmu.edu/scs25/history"]
# urls = ["https://www.cmu.edu/about/history.html"]
urls = ["https://www.cmu.edu/news/stories/archives/2019/april/spring-carnival-buggy.html"]
# remove_list = ["Search", "CMU on Instagram", "CMU on Facebook", "CMU on Twitter", "Search this site only", "© 2024 Carnegie Mellon University"]

def scrape_word(urls): 
    out = []
    for url in urls:
        response = requests.get(url, timeout=10)
        print(response.status_code)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        words = str(soup.get_text()).strip()
        sentences = [i.strip() for i in words.split("\n")]
        sentences = [i for i in sentences if len(i) != 0]
        print(soup)
        # hrefs = []
        # for a in soup.find_all('a', href=True):
        #     if "html" in a['href']:
        #         print(a['href'])
        #         hrefs.append(a['href'])
        # hrefs = list(set(hrefs))
        mydivs = soup.find_all("div", {"class": "tl-text"})
        print(mydivs)
        # for i in hrefs:
        #     response = requests.get(url+i, timeout=5)
        #     soup = BeautifulSoup(response.content, 'html.parser')
        #     words = str(soup.get_text()).strip()
        #     s = [i.strip() for i in words.split("\n")]
        #     s = [i for i in s if len(i) != 0]
        #     sentences.extend(s)
        out.extend(sentences)

    # with open('buggy.txt', 'w') as f:
    #     for i in out:
    #         f.write(i)
    #         f.write("\n")

scrape_word(urls)
