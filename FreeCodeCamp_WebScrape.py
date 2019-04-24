# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:27:05 2019

@author: Joubert
"""

#https://www.freecodecamp.org/news/
import requests
from bs4 import BeautifulSoup
from csv import writer

r = requests.get("https://www.freecodecamp.org/news/")
soup = BeautifulSoup(r.text, "html.parser")
posts = soup.find_all("article") 

with open("FreeCodeCamp_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title","URL"])
    
    for article in posts:
     #find the 'a' tag in the HTML
     a_tag = article.find("a")
     title = article.find("h2").get_text()
     #find the links to articles.
     link = a_tag['href']
     csv_writer.writerow([title,link])