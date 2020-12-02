# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다.".format(language))


# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())


# print(dir(random))


# lst = [1,2,3]
# print(dir(lst))

# name = "jain"
# print(dir(name))

# ########################외장 함수
# import glob #확장자가 py 인 모든 파일 알려줌.
# print(glob.glob("*.py"))

# os
# import os
# print(os.getcwd())  #현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.removedirs(folder)
#     print("폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print("폴더를 생성")


# print(os.listdir())


# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))


import datetime
# print("오늘 날짜는 ", datetime.date.today())


today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 {0}".format(today + td))