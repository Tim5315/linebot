import requests
from bs4 import BeautifulSoup
from opencc import OpenCC

def getinfo(name):
    try:
        cc = OpenCC('s2tw')
        url = 'https://www.sin80.com/artist/' + name
        url2 = 'https://www.sin80.com/en/artist/' + name
        back = []
        data = requests.get(url)
        bs = BeautifulSoup(data.text, "lxml")
        record = bs.findAll('div',{'class':'bd bulletin-content'})
        record = record[0].text.replace(' ', '').replace('\n', '')
        back.append(cc.convert(record))
        data2 = requests.get(url2)
        bs2 = BeautifulSoup(data2.text, "lxml")
        works = bs2.findAll('table', {'class':'worklist'})[-1]
        back.append(works.text.replace(' ', '').split()[0])
        return back
    except:
        return '查無資料'
