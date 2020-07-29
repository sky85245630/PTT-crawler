import requests
from bs4 import BeautifulSoup
import html5lib
import time



#先印出時間，再把前面的0拿掉
today = time.strftime('%m/%d').lstrip('0')
print(today)

def Gossiping(url):
    resp = requests.get(url)
    # URL錯誤回報
    if resp.status_code != 200:
        print('URL發生錯誤' + url)
        return
    # 匯入html5lib
    soup = BeautifulSoup(resp.text, 'html5lib')
    # 找到他上一頁的元素在div裡面的btn-group btn-group-paging class
    paging = soup.find('div','btn-group btn-group-paging')
    # 再找到div裡面的a元素（總共有四個 要拿到第二個元素）在取得href裡面的文字
    paging.find_all('a')[1]['href']

    #裡面放文章
    articles=[]

    #找到所有為r-ent 的 div元素
    rents = soup.find_all('div','r-ent')
    for rent in rents:
        # 標題
        title = rent.find('div','title').text.strip()
        # 推文數
        count = rent.find('div','nrec').text.strip()
        # 時間
        date = rent.find('div','meta').find('div','date').text.strip()

