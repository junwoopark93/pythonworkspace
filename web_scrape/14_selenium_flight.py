from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/flights"
browser.get(url)

#가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

#이번달 27일 다음달 28일 선택
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[1].click()


#그 다음달 선택해보기

browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()


#제주도 선택
browser.find_element_by_xpath("//*[@id=\"recommendationList\"]/ul/li[1]/div/span").click()


# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()


# 첫번째 결과 출력
#elem = browser.find_element_by_xpath("//*[@id=\"content\"]/div[2]/div/div[4]/ul/li[1]")

# 10초간 기다리되 그 전에 작업이 완료되면 바로 실행.
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div/div[4]/ul/li[1]")))
    #성공했을 때 동작 수행
    print(elem.text)
finally:
    browser.quit()

print(elem.text)