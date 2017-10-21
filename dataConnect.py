import requests
from bs4 import BeautifulSoup as bs
import tokenize_new

def getData(link):
    try:
        content = requests.get(link).content
    except:
        print("Cannot connect")
        return -1
    html_soup = bs(content , "lxml")
    page_links = []
    tokens = []
    for i in html_soup.find_all("a"):
        if i.get("href") not in page_links:
            page_links.append(i.get("href"))
    page_links = linkProcess(link, page_links)
    #textTags = ['meta' , 'p' , 'h1' , 'h2' , 'h3', 'h4' , 'h5' , 'h6' , 'title' , 'article' , 'div' , 'strong']
    for script in html_soup(["script" , "style"]):
        script.extract()

    text = html_soup.get_text()
    text = text.split('\n')
    text = [x for x in text if x != '']
    text = [x.strip() for x in text]

    for i in range(len(text)):
        temp_word_list = tokenize_new.tokenized_text(text[i])
        for j in temp_word_list:
            if j not in tokens:
                tokens.append(j)


    return page_links, tokens

def linkProcess(seed, listLink):
    new_list = []
    for i in listLink:
        if i != None:
            temp = i
            if len(temp) > 2:
                if i == '#':
                    continue
                elif i[0] == '#':
                    continue
                elif i[0] == '/' and i[1] != '/':
                    temp = seed + i[1:]
                elif i[0] == '/' and i[1] == '/':
                    temp = i[2:]

            if "http" in temp:
                pass
            elif "https" not in temp:
                temp = "https://" + temp
            new_list.append(temp)
    return new_list