print(2**3)
print(5%3)
print(10%3)
print(5//3)
print(10//3)


print(abs(-5))
print(pow(4,2))
print(max(5,22))
print(min(2,34))
print(round(3.14))


from math import *
print(floor(4.99))
print(ceil(3.25))
print(sqrt(16))

from random import *

print(random())
print(random() * 10)
print(int(random() * 10))
print(1 + int(random() * 10))
print(1 + int(random() * 10))
print(1 + int(random() * 10))
print(1 + int(random() * 10))
print(1 + int(random() * 10))
print(1 + int(random() * 10))
print(1 + int(random() * 10))

print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))
print(randrange(1,46))

print(randint(1,45))



python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)


print(python.find("n"))
print(python.find("Java")) #없으면 -1
#index 의 경우 없으면 에러

print(python.count("n"))


print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %s로 시작해요." % "A")

print("나느 %s색과 %s색을 좋아해요. " % ("파란", "빨간"))
print("나는 {}살 입니다.".format(20)) 

print("나느 {}과 {}색을 좋아해요. ".format("파란", "빨간"))
print("나느 {0}과 {1}색을 좋아해요. ".format("파란", "빨간"))
print("나느 {1}과 {0}색을 좋아해요. ".format("파란", "빨간"))

print("나느 {age}과 {color}색을 좋아해요. ".format(age = 20, color = "빨강"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")
print("저는 '나도코딩'입니다.")

print("C:\\pythonworkspace\\pygame_basic")
print("Red Apple\rPine") # 맨앞으로 커서 이동
print("Redd\b Apple")
print("Red\tApple")

#비밀번호 만들어주는 프로그램
url = "http://www.naver.com"
my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는  {1} 입니다.".format(url, password))


#사전

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) # 에러 발생, 없는 키.
print(cabinet.get(5, "사용가능")) # 에러발생x , 없으면 사용가능 표시
print("hi")

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)


#튜플 변경되지 않는 리스트
menu = ("돈까스" , "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") 값추가 오류

#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#집합
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

print(java & python) #교집합
print(java.intersection(python))

print(java | python) #합집합
print(java.union(python))

print(java - python) # 차집합
print(java.difference(python))

python.add("김태호")
print(python)

python.remove("김태호")
print(python)



#자료 구조 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


#셔플 프로젝트

lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))

users = range(1, 21)
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print(" 당첨자 발표 ")
print(" 치킨 당첨자 : {}".format(winners[0]))
print(" 커피 당첨자 : {}".format(winners[1:]))

#입력받아 분기하기

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요")
# elif 10 <= temp and temp <30:
#     print("괜찮아 보이네요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요")


#반복문

for waiting_no in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(30):
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


""" customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index += 1 """

""" absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue #스킵해라.
    if student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와라".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


students = [1,2,3,4,5]
print(students)
students= [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) """


""" students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) """


""" cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 ( 소요시간 : {1}분)".format(i,time))
        cnt +=1
    else:
        print("[ ] {0}번째 손님 ( 소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 : {0} 분".format(cnt)) """

""" def profile(name, age, *language): #가변인자.
    print("이름 : {0}\t 나이 : {1} \t".format(name, age), end = " ")
    for lang in language:
        print(lang, end= " ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JAVA Script")
profile("김태호", 25, "Kotlin", "Swift") """


""" gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(gun)

def checkpoint_ret(gun, soldiers):
    gun
    gun = gun - soldiers
    print(gun)
    return gun

print(gun)
gun = checkpoint_ret(gun, 2)
print(gun) """


print("Python","Java","C++", sep=",", end="?")
print("무엇이 더 재밌을까요?")