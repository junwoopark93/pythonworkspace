import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes"}
res = requests.get(url,headers=headers)
print("응답코드 :", res.status_code)
with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)