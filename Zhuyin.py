import requests
from bs4 import BeautifulSoup
def read( word ):
    phone = ''
    try:
        url = f'https://dict.revised.moe.edu.tw/search.jsp?md=1&word={word}#searchL'
        html = requests.get(url)
        bs = BeautifulSoup(html.text, features="lxml")

        data = bs.find('table', id='searchL')
        row = data.find_all('tr')[2]
        chinese = row.find('cr').text
        phone += row.find('td', class_='ph').text
    except:
        for i in word:
            url = f'https://dict.revised.moe.edu.tw/search.jsp?md=1&word={i}#searchL'
            html = requests.get(url)
            bs = BeautifulSoup(html.text, features="lxml")
            data = bs.find('table', id='searchL')
            row = data.find_all('tr')[2]
            chinese = row.find('cr').text
            phone += row.find('td', class_='ph').text
    return('長時間查詢中\n', phone)
