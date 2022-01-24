import re
import datetime
import requests
import csv
from bs4 import BeautifulSoup
url = "http://xsc.sicau.edu.cn/Web/NewsList-LJw34Jmu~aacgacac.html?PNodeNum=00260202"
urlbefore = "http://xsc.sicau.edu.cn/Web/"
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#Content > li')
file = open('noticelist.txt','w')
#print(data)
for item in data:
    print(item)
    datestr = str(item.select('span'))
    match = re.search("(\d{4}-\d{1,2}-\d{1,2})", datestr)
    datetrue = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    result={
        'title' : item.get_text(),
        'link' : urlbefore+item.a.attrs.get('href'),
        'date' : str(datetrue)
        }
    for key,values in result.items():
        file.write(key)
        file.write(':')
        file.write(values)
        file.write('    ')
    file.write('\r\n')
file.close()