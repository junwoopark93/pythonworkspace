#pip install selenium   ->셀레니움을 통해 브라우저 통제 가능
#chrome driver 설치, chrome://version
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()    # 경로 입력해 주어야 함. "./chromedriver.exe"
browser.get("http://naver.com")
# elem = browser.find_element_by_class_name("link_login")
# elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()
elem = browser.find_element_by_id("query")

elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_tag_name("a")
elem = browser.find_elements_by_tag_name("a")

# for e in elem:
#     result = e.get_attribute("href")
#     print(result)
    
browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
print(elem)
elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath("//*[@id=\"daumSearch\"]/fieldset/div/div/button[2]")
elem.click()
browser.quit()  #close는 한개 탭 닫기.
#print(elem)