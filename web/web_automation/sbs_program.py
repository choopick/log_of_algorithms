import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['기간', '순위', '프로그램', '시청률'])
name = list()
for i in range(2010, 2019):
    for j in range(1, 13):
        for k in range(5):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(i,j,k)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for tr_tag in soup.select('tr')[1:]:
                td_tags = tr_tag.select('td')
                period = "{}년 {}월 {}주차".format(i, j, k + 1)
                row = [
                    period,
                    td_tags[0].get_text(),
                    td_tags[2].get_text(),
                    td_tags[3].get_text()
                ]
                if td_tags[1].get_text() == 'SBS':
                    ws.append(row)

wb.save('SBS_데이터.xlsx')