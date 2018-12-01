from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off').content

soup = BeautifulSoup(source, 'html.parser')

# For Single Data
for article in soup.find('div'):

    headline = article.find('div', class_='_3wU53n').text
    print(headline)

    price = article.find('div',class_='_1vC4OE').text
    print(f'Price: {price}')

    print('Specifications:-')
    for detail in article.find('ul', class_='vFw0gD').find_all('li', class_='tVe95H'):
        print(detail.text)
        
    print()

# For multiple data
#TODO:-