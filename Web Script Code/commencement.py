import requests 
from bs4 import BeautifulSoup 
import time 

results = {}
url = "https://www.cmu.edu/commencement/schedule"
remove_list = ["Search", "CMU on Instagram", "CMU on Facebook", "CMU on Twitter", "Search this site only", "© 2024 Carnegie Mellon University"]

def scrape_word(url): 
    response = requests.get(url, timeout=5)
    if (response.status_code == 404):
        print("404")
        return
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
    for i in hrefs:
        response = requests.get(url+i, timeout=5)
        if (response.status_code == 404):
            print("404")
            return
        soup = BeautifulSoup(response.content, 'html.parser')
        words = str(soup.get_text()).strip()
        s = [i.strip() for i in words.split("\n")]
        s = [i for i in s if len(i) != 0]
        s = list(filter(lambda x: x not in remove_list, s))
        sentences.extend(s)

    with open('commencement.txt', 'w') as f:
        for i in sentences:
            f.write(i)
            f.write("\n")
    # print(text_content.split("\n"))
    # print(soup)
    # # Look only at the main content div or else you'll get other undesired tags
    # soup = soup.find('div', attrs={'class': 'css-1kc5m8x e1qo4u830'})
    # # The below variable is the class used by Thesaurus.com for synonyms
    # word_class = 'css-133coio etbu2a32'
    # # Structure of site is spans hold links which have text of the word
    # spanList = soup.find_all('span', attrs={'class': word_class})
    # synList = [span.find('a').text for span in spanList]
    # results[word] = synList
scrape_word(url)
