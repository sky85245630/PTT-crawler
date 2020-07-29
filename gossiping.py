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




