# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 21:56:36 2016

@author: Andy
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LanguageLick.settings")
from translator.models import *
import feedparser
import urllib
from bs4 import BeautifulSoup
import codecs
import datetime


previously_inserted_articles = Article.objects.all()
previously_inserted_headlines = []
for a in previously_inserted_articles:
    previously_inserted_headlines.append(a.headline)


##RSS Feeds
yahoo_EEUU = "https://es.noticias.yahoo.com/rss/estados-unidos"
yahoo_deportes = "https://es.noticias.yahoo.com/rss/deportes"
yahoo_americaLatina = "https://es.noticias.yahoo.com/rss/america-latina"
yahoo_economia = "https://es.noticias.yahoo.com/rss/economia"

bbc_recent = "http://www.bbc.co.uk/mundo/ultimas_noticias/index.xml"
bbc_tech = "http://www.bbc.co.uk/mundo/temas/tecnologia/index.xml"
bbc_cultura = "http://www.bbc.co.uk/mundo/temas/cultura/index.xml"
bbc_economia = "http://www.bbc.co.uk/mundo/temas/economia/index.xml"

cnn_espanol = "http://cnnespanol.cnn.com/feed/"

feed_yahoo_EEUU = feedparser.parse(yahoo_EEUU)
feed_yahoo_deportes = feedparser.parse(yahoo_deportes)
feed_yahoo_americaLatina = feedparser.parse(yahoo_americaLatina)
feed_yahoo_economia = feedparser.parse(yahoo_economia)

links = []

count = 0
for item in feed_yahoo_EEUU["entries"]:
    links.append((item["published"],"yahoo_EEUU",item["link"]))
    count += 1
    if count >3:
        break
    
count = 0
for item in feed_yahoo_deportes["entries"]:
    links.append((item["published"],"yahoo_deportes",item["link"]))
    count += 1
    if count >3:
        break
    
count = 0
for item in feed_yahoo_americaLatina["entries"]:
    links.append((item["published"],"yahoo_americaLatina",item["link"]))
    count += 1
    if count >3:
        break
    
count = 0
for item in feed_yahoo_economia["entries"]:
    links.append((item["published"],"yahoo_economia",item["link"]))
    count += 1
    if count >3:
        break
    
for link in links:
    url = link[2]
    date = link[0]
    source = link[1]
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r,'lxml')
    
    title_class = "Lh(1.1) Fz(25px)--sm Fz(32px) Mb(17px)--sm Mb(20px) Mb(30px)--lg Ff($ff-primary) Lts($lspacing-md) Fw($fweight) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) Wow(bw)"
    title_type = "h1"
    
    author_class = "C(#222)"
    author_type = "a"
    
    date_class = "date D(ib)"
    date_type = "span"
    
    text_class = "canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm canvas-atom"
    text_type = "p"
    
    title_list = soup.find_all(title_type,class_=title_class)
    author_list = soup.find_all(author_type,class_=author_class)
    date_list = soup.find_all(date_type,class_=date_class)
    text_list = soup.find_all(text_type,class_=text_class)
    
    title = ""
    author = ""
    date = ""
    text = ""
    newline=u'\n'
    
    for x in title_list:
        title+=x.get_text()
        
    for x in author_list:
        author+=x.get_text()
        
    for x in date_list:
        date+=x.get_text()
        
    for x in text_list:
        text+=x.get_text()
    
    if len(title_list) != 1 or title in previously_inserted_headlines:
        continue
    else:
        try:
            article_obj = Article(headline=title,date_added=datetime.datetime.utcnow(),file_name=str(doc_id)+".txt",article_source=source,good_file=True)
            article_obj.save()
        except Exception:
            print("Failed to create DB object: "+link[2])
            print("From group: " + link[1])
            print(traceback.format_exc())
            continue
        doc_id = article_obj.id
        with codecs.open("translator/texts/"+str(doc_id)+".txt", "w", "ISO-8859-1") as textfile:
            try:            
                textfile.write(title)
                textfile.write(newline)
                textfile.write("-----")
                textfile.write(newline)
                textfile.write(author)
                textfile.write(newline)
                textfile.write("-----")
                textfile.write(newline)
                textfile.write(date)
                textfile.write(newline)
                textfile.write("-----")
                textfile.write(newline)
                textfile.write(text)
            except Exception:
                article_obj.good_file=False
                article_obj.save()
                print("Failed to insert: "+link[2])
                print("From group: " + link[1])
                print(traceback.format_exc())
                continue
        
    

    
