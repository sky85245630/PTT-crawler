import requests
from bs4 import BeautifulSoup
# import html5lib
import time

resp = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(resp.text, 'html5lib')

#先印出時間，再把前面的0拿掉
today = time.strftime('%m/%d').lstrip('0')
print(today)

