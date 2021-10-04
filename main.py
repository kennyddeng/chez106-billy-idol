import requests
from bs4 import BeautifulSoup

"""
dab = requests.text('https://www.chez106.com/recently-played/')
html_text = requests.get('https://www.chez106.com/recently-played/').text
soup = BeautifulSoup(html_text, 'lxml')
print(html_text)
results = soup.find_all('li', class_='row decibel-border-bottom-color-first')
print(results)
print(len(results))
soup.get_text()


#for i in range(len(results)):
#    print(results[i])

"""
html_text = requests.get('https://woodgears.ca/').text
soup = BeautifulSoup(html_text, 'lxml')
print(html_text)