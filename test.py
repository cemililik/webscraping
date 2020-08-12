import requests
import time
from bs4 import BeautifulSoup
from csv import writer
from csv import reader

filename = 'test.csv'
with open(filename, 'w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Category', 'Title', ' Location']
        csv_writer.writerow(headers)

link2 = 'https://www.houzz.com/professionals/architects-and-building-designers/brandon-architects-inc-pfvwus-pf~1291854741'
response = requests.get(link2)
soup = BeautifulSoup(response.text,'lxml') 
with open(filename, 'a') as csv_file:
    csv_writer = writer(csv_file)  
    
    # page_soup = soup(ret.text, 'lxml')
    data = soup.select("[type='application/ld+json']")
    # title = soup.find('application/ld+json')
    # titletext = title.text

    # category = soup.find(id_='profile_meta_proType')
    # categorytext = category.a.text

    # print(categorytext)
    print(data)
    


    
    csv_writer.writerow(data)