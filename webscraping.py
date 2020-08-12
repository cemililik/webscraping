import requests
import time
from bs4 import BeautifulSoup
from csv import writer
from csv import reader

filename = 'cabinets_.csv'
with open(filename, 'w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Title', ' Link']
        csv_writer.writerow(headers)

i=0
while i < 1500:
    linkilk = 'https://www.houzz.com/professionals/cabinets/c/Orange-County--CA'+str(i)
    response = requests.get(linkilk)
    soup = BeautifulSoup(response.text,'lxml')
    companies = soup.find_all(class_='hz-pro-search-results__item')

    with open(filename, 'a') as csv_file:
        csv_writer = writer(csv_file)        
        for company in companies:
            title = company.find(class_='header-5 text-unbold mlm').get_text()
            link = company.find('a')["href"]
            csv_writer.writerow([title, link])

    print(i)
    print(linkilk)
    i = i + 15

        








