import json
import os
import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.goodreads.com/book/show/4214.Life_of_Pi" , verify= False) #instructiune pentru accesarea paginii html

soup = BeautifulSoup(page.content, "html.parser") #pentru parsarea/parcurgerea paginii

reviews_name = soup.find_all('div', {'class': 'ReviewerProfile__name'}) #elementele html care contin clasa cu numele celor ce au lasat review
reviews_date = soup.find_all('section', {'class': 'ReviewCard__row'}) #elementele html care contin clasa cu data cand a fost scris review
reviews_content = soup.find_all('section', {'class': 'ReviewText__content'}) #elementele html care contin clasa cu textul care a fost scris ca si review

data = list() #lista care contine detaliile despre reviews

if len(reviews_name) == len(reviews_date) == len(reviews_content): #verific daca sunt acelasi numar de elemente

    for name, date, content in zip(reviews_name, reviews_date, reviews_content): #se face iterarea listelor create la liniile 11, 12, 13
        review_data = {} #se creeaza dictionarul
        review_data['author'] = name.get_text(strip=True) #se extrage numele celui ce a lasat review-ul
        review_data['date'] = date.get_text(strip=True)   #se extrage data cand a fost lasat review-ul
        review_data['text'] = content.get_text(strip=True) #se extrage textul care a fost lasat ca si review
        data.append(review_data)  #se adauga dictionarul in lista
    print(f"this is {data}")  #se printeaza rezultatul
else:
    print("Difera lungimea elementelor extrase.") #se printeaza mesajul in cazul in care numarul de elemente este diferit

if not os.path.isdir("reviews.json"): #se verifica daca exista folderul, daca nu
   os.mkdir("reviews.json")      #se face creearea lui
with open("reviews.json/adn.json", "w") as f: #se dechide un fisier json pentru a scrie in el
   json.dump(data, f, indent=4) #se adauga rezultatul in fisierul json

#https://realpython.com/beautiful-soup-web-scraper-python/
#https://pypi.org/project/beautifulsoup4/
#https://www.w3schools.com/
#https://www.geeksforgeeks.org/