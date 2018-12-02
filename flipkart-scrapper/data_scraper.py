from bs4 import BeautifulSoup
import requests
import csv
from array import array

source = requests.get('https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off').content

soup = BeautifulSoup(source, 'html.parser')

csv_file = open('flipkart_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name','Price','Specifications'])

for article in soup.find_all('div',class_='_1UoZlX'):
    headline = article.find('div',class_='_3wU53n').text
    print(headline)

    price = article.find('div',class_='_1vC4OE').text
    print(f'Price: {price}')

    print('Specification:-')
    specs=[]
    for detail in article.find('ul',class_='vFw0gD').find_all('li',class_='tVe95H'):
        specs.append(detail.text)
        
    final_detail = ', '.join(specs)
    print(final_detail)


    print()

    csv_writer.writerow([headline,price,final_detail])

csv_file.close()