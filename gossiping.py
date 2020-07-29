import requests
from bs4 import BeautifulSoup
import html5lib

resp = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(resp.text, 'html5lib')
