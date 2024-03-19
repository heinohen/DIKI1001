# Imports
import spacy 
import pandas as pd
from spacytextblob import spacytextblob
from bs4 import BeautifulSoup
import requests

# Loaders
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")
df = pd.read_csv("urls.csv")
urls = df["Address"].tolist()

# Get text from url's
for count, x in enumerate(urls):
    url_sent_score = []
    url_sent_label = [] 
    url = x
    print(url)

    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    res = requests.get(url,headers=headers)
    html_page = res.text

    ###### bs4 part
    soup = BeautifulSoup(html_page, 'html.parser')
    print("Title of the website is : ")
    for title in soup.find_all('title'):
        print(title.get_text())
    for script in soup(["script", "style","meta","label","header","footer"]):
        script.decompose()
    page_text = (soup.get_text()).lower()
    page_text = page_text.strip().replace("  ","")
    page_text = "".join([s for s in page_text.splitlines(True) if s.strip("\r\n")])
    

    #######

    # Actual nlp part
    doc = nlp(page_text)
    sentiment = doc._.blob.polarity
    sentiment = round(sentiment, 2)
    
    if sentiment > 0:
        sent_label = "positive"
    else:
        sent_label = "negative"
    
    url_sent_label.append(sent_label)
    url_sent_score.append(sentiment)

    # words 
    pos_words = dict()
    neg_words = dict()

    for x in doc._.blob.sentiment_assessments.assessments:
        word = x[0][0]
        if x[1] > 0:
            if word not in pos_words.keys():
                pos_words[word] = 1
            else:
                pos_words[word] += 1
        elif x[1] < 0:
            if word not in neg_words.keys():
                neg_words[word] = 1
            else:
                neg_words[word] += 1
        else:
            pass
    
    print(f'Most frequent positive words:')
    for i in sorted(pos_words.keys(), key = lambda x:pos_words[x], reverse = True)[:5]:
        print(i, pos_words[i])
    print("\n")
    print(f'Most frequent negative words:')
    for i in sorted(neg_words.keys(), key = lambda x:neg_words[x], reverse = True)[:5]:
        print(i, neg_words[i])

    for x in enumerate(url_sent_score):
        if x[1] > 0:
            print(f'{url_sent_score, sent_label}\U0001F600')
        elif x[1] < 0:
            print(f'{url_sent_score, sent_label}\U0001F92E')
        else:
            pass
    print("\n")



