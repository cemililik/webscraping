import requests
import time
from bs4 import BeautifulSoup
from csv import writer
from csv import reader

filename = 'Companies3.csv'
with open(filename, 'w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Category', 'Title', ' Link']
        csv_writer.writerow(headers)

with open('Categories.csv','r') as csv_file:
    csv_reader = reader(csv_file)
    for line in csv_reader:
        # print(line[1])
        i=0
        while i < 1500:
            linkilk = line[1]
            linkilk2 = linkilk + str(i)
            response = requests.get(linkilk2)
            soup = BeautifulSoup(response.text,'lxml') 
            companies = soup.find_all(class_='hz-pro-search-results__item')
            with open(filename, 'a') as csv_file:
                csv_writer = writer(csv_file)        
                for company in companies:
                    title = company.find(class_='header-5 text-unbold mlm').get_text()
                    link = company.find('a')["href"]
                    category = line[0]
                    csv_writer.writerow([category, title, link])
            i = i + 15

    print(i)
    print(linkilk)
    