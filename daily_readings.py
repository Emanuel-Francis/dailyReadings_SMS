from bs4 import BeautifulSoup
import requests

def send():
    url= "https://www.catholic.org/bible/daily_reading/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results= soup.find(id='bibleDailyReading')
    readings = results.find_all('div', class_='col-md-6')

    infoList= []
    for next in readings:
        infoList.append(next)

    #print(infoList[1].text)
    return infoList[1].text

    

#print(soup)
