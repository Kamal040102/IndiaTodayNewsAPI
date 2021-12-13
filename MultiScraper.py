from bs4 import BeautifulSoup
import requests

'''
    Categories:
        India
        World
        Business
        Science
'''

class MultiScraper():
    def findNews(self, type, type2):
        lstNews = []
        url = requests.get(f"https://www.indiatoday.in/{type}?{type2}").text

        soup = BeautifulSoup(url, 'lxml')
        newsList = soup.find_all('div', class_='catagory-listing')
        for newsItem in newsList:    
            newsData = newsItem.find('div',class_='detail')
            newsPic = newsItem.find('div', class_='pic')
            newsTitle = newsData.find('a').contents[0]
            newsDescription = newsData.find('p').text
            newsUrl = newsData.find('a')['href']
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
