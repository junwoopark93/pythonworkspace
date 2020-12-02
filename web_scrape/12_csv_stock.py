import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "시가총액1-200"
f = open(filename, "w", encoding="utf-8-sig", newline="")    #newline을 써줘야 한줄마다 엔터가 안들어감.(자동 줄바꿈 방지, 2줄마다 띄워지는 것을 방지)
writer = csv.writer(f)      #엑셀파일 안깨지게 utf-8-sig

#제목 쓰기.
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# ["N", "종목명", "현재가", ...]
print(type(title))
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows =  soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]        #strip 불필요한 공백 제거.
        # print(data)

        writer.writerow(data)
