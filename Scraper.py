from bs4 import BeautifulSoup
import requests
import random

'''
    Categories:
        India
        World
        Business
        Science
'''

class Scraper():
    def findNews(self, type):
        lstNews = []
        url = requests.get(f"https://www.indiatoday.in/{type}").text
        soup = BeautifulSoup(url, 'lxml')
        newsList = soup.find_all('div', class_='catagory-listing')
        for newsItem in newsList:
            
            newsData = newsItem.find('div',class_='detail')
            newsPic = newsItem.find('div', class_='pic')
            newsTitle = newsData.find('a').contents[0]
            newsUrl = newsData.find('a')['href']
            newsDescription = newsData.find('p').text
            newsPicUrl = newsPic.find('img')['src']
            # print(newsUrl, newsTitle, newsDescription, newsPicUrl)
            item= {
                'newsTitle': newsTitle,
                'newsDescription': newsDescription.replace("\n", " "),
                'newsURL' : f"https://www.indiatoday.in{newsUrl}",
                'newsPicURL' : newsPicUrl
            }
            lstNews.append(item)
        MainItem = {
            "source": "https://www.indiatoday.in",
            "endPoints": ['/world','/business','/science'],
            "articles": lstNews
        }

        return MainItem
