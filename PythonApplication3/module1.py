from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import datetime
import requests
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup

url = "http://xsc.sicau.edu.cn/Web/NewsList-LJw34Jmu~aacgacac.html?PNodeNum=00260202"
urlbefore = "http://xsc.sicau.edu.cn/Web/"
pagenumber = 1
serialnumber = 1
options = Options()
options.use_chromium = True
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_experimental_option('excludeSwitches',['enable-automation'])
driver = webdriver.Edge("msedgedriver.exe",options = options)
file = open('noticelist.txt','w')
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'lxml')
data = soup.select('#Content > li')
totallist = soup.select('#lblRecordCount')
totalpage = soup.select('#lblPageCount')
for item in totallist:
    totallistnumber = int(item.get_text())
for item in totalpage:
    totalpagenumber = int(item.get_text())
while pagenumber <= totalpagenumber:
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    data = soup.select('#Content > li')
    currentpage = soup.select('#lblCurrentPage')
    for item in currentpage:
        currentpagenumber = int(item.get_text())
    print("当前爬取到%d页，共计%d页，剩余%d页"%(currentpagenumber,totalpagenumber,totalpagenumber-currentpagenumber))
    for item in data:
        datestr = str(item.select('span'))
        match = re.search("(\d{4}-\d{1,2}-\d{1,2})", datestr)
        datetrue = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
        result={
            'serialnumber' : str(serialnumber),
            'Title' : item.get_text(),
            'Link' : urlbefore+item.a.attrs.get('href'),
            'Date' : str(datetrue)
            }
        for key,values in result.items():
            file.write(key)
            file.write(':')
            file.write(values)
            file.write('\r\n')
        file.write('\r\n')
        serialnumber += 1
    nextpagebutton = driver.find_element(By.ID,"lbnNextPage")
    nextpagebutton.click()
    pagenumber += 1
file.close()
driver.quit()
serialnumber = int(serialnumber)
print("爬取完毕，总计通知%d条，成功爬取%d条。"%(totallistnumber,serialnumber-1))