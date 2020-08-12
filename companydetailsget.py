import requests
import time
from bs4 import BeautifulSoup
from csv import writer
from csv import reader

filename = 'CompanyDetails3.csv'
with open(filename, 'w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['Category', 'Title']
        csv_writer.writerow(headers)

with open('Companies_v3.csv','r') as csv_file:
    csv_reader = reader(csv_file)
    for line in csv_reader:
        link2 = line[2]
        response = requests.get(link2)
        soup = BeautifulSoup(response.text,'lxml') 
        with open(filename, 'a') as csv_file:
            csv_writer = writer(csv_file)  
            title = soup.select("[type='application/ld+json']")
            category = line[0]
            
            csv_writer.writerow([category, title])
    # print(i)
    # print(linkilk)
    




