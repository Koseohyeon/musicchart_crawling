from openpyxl import Workbook
from bs4 import BeautifulSoup
import requests
url='https://music.bugs.co.kr/chart'
r=requests.get(url)#requests의 get 함수 사용
html=r.text
soup=BeautifulSoup(html,'html.parser')#text를 parser분석
#응답확인
#print(url)
#print(r)

title=soup.select('p.title')
artist=soup.select('p.artist')
for i in range(len(title)) :
    Title=title[i].text.strip().split('\n')[0]
    Artist=artist[i].text.strip().split('\n')[0]
    print('{:3} 위 {}-{}'.format(i+1,Title,Artist))

#엑셀파일
wb=Workbook()
wb.sheetnames
ws=wb.active

for i in range(len(title)) :
    ws.append([i+1,Title,Artist])

wb.save("TOP_100.xlsx")


