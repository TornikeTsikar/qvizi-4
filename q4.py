import requests
from bs4 import BeautifulSoup
import csv

with open('binebi.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])

    for page in range(1, 6):
        url = f'https://binebi.ge/gancxadebebi?city=1&page={page}&sort=id%2Cdesc'
        response = requests.get(url)

        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            apt_soup = soup.find('div', class_="search-item-container")

            if apt_soup:
                all_apt = apt_soup.find_all('div', class_='list-item')
                for apt in all_apt:
                    apt_div = apt.find('div', class_='item-info')
                    if apt_div:
                        title = apt_div.a.text.strip() if apt_div.a else 'No title'
                        price_element = apt_div.find('div', class_='item-price')
                        price = price_element.text.strip() if price_element else 'No price'

                        writer.writerow([title, price])
                        print(title, price)
        else:
            print(f'Failed to retrieve page {page}')
