print("start BeautifulSoup script")

from bs4 import BeautifulSoup
import requests 
from csv import writer 

# get web page information
url = "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
  writer = writer(f)
  header = ['Name', 'Area', 'Price']
  writer.writerow(header)
  
  for list in lists:
    title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
    price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
    area = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')

    info = [title, area, price]
    writer.writerow(info)

print("BeautifulSoup Script finished")
  



