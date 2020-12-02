from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()    # 경로 입력해 주어야 함. "./chromedriver.exe"
browser.get("http://naver.com")

#로그인 버튼 누르기
elem = browser.find_element_by_class_name("link_login")
elem.click()

#id 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

#로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

#5, id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#brower.close()
browser.quit()