import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)   #처음으로 발견되는 a 엘리먼트를 표시해주세요.
# print(soup.a.attrs)   #처음으로 발견되는 a 엘리먼트의 속성정보를 표시해주세요.
# print(soup.a["href"]) # a 엘리먼트의 href 속성 값을 표시해주세요.

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))    #class ="Nbtn_upload" 인 a element 를 찾아주세요
# print(soup.find(attrs={"class":"Nbtn_upload"}))    #class ="Nbtn_upload" 인 어떤 element 를 찾아주세요

# rank1 = soup.find("li", attrs = {"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling
# rank3 = rank1.next_sibling.next_sibling
# print(rank2)
# print(rank3)

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2)
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))


webtoon = soup.find("a", text="관계의 종말-29화")
print(webtoon)