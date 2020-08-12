import requests
import time
from bs4 import BeautifulSoup
from csv import writer
from csv import reader

filename = 'Categories.csv'
with open(filename, 'w') as csv_file:
        csv_writer = writer(csv_file)
        # headers = ['Title', ' Link']
        # csv_writer.writerow(headers)


linkilk = 'https://www.houzz.com/professionals/c/Orange-County--CA'
response = requests.get(linkilk)
soup = BeautifulSoup(response.text,'lxml')
companies = soup.find_all(class_='br-carousel-item mts mbm')

with open(filename, 'a') as csv_file:
    csv_writer = writer(csv_file)        
    for company in companies:
        title = company.find(class_='hz-text-clamp__text-node').get_text()
        link = company.find('a')["href"]
        csv_writer.writerow([title, link])

            








