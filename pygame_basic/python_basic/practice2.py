import sys

# 표준 출력.
""" 
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)    #에러 처리 가능

scores = {"수학" : 0, "영어" :50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") """

#입력 하기

""" 
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) #0으로 채우기.

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 {}".format(answer)+" 입니다.") """

# 숫자 표시

""" print("{0: >10}".format(523523))
print("{0: >+10}".format(523523))
print("{0: >+10}".format(-523523))

print("{0:_<+10}".format(523523))
print("{0:_<+10}".format(-523523))

print("{0:,}".format(5235212313123123133))
print("{0:+,}".format(5235212313123123133))
print("{0:+,}".format(-5235212313123123133))

print("{0:^<+50,}".format(5235212313123123133))

print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) """


# 파일 입출력

""" score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() """

#쓰기 - 더하기
""" score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close() """

#읽기
""" score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close() """


#한줄씩 읽기.
""" score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close() """


""" score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close() """


""" score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close() """

import pickle # pickle을 이용해야 피클파일을 읽을 수 있음.
""" profile_file = open("profile.pickle", "wb") #binary
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close() """

""" profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close() """

#with를 쓰면 파일 입출력 더욱 쉽다. close를 안해도 된다.
""" 
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) """
#일반 파일
""" 
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부합니다.") """

""" with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read()) """

# 예제 연습하기.
""" for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0}주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :") """

# 모듈 - class

""" name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

#탱크
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을공격합니다. [공격력 {2}]". format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "12시", tank_damage) """

""" class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage)) """
""" 

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름"" : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name)) """

""" class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp -= damage
         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
         if self.hp <=0:
             print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25) """


# 상속.

""" class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit): # 상속받기.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp -= damage
         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
         if self.hp <=0:
             print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

#다중 상속 - 드랍쉽을 만들어보자
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리 
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") """

#오버로딩

 
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed)) 


# class AttackUnit(Unit): # 상속받기.
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#          print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#          self.hp -= damage
#          print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#          if self.hp <=0:
#              print("{0} : 파괴되었습니다.".format(self.name))

# #다중 상속 - 드랍쉽을 만들어보자
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
#         Flyable.__init__(self, flying_speed)
    
#     def move(self, location):
#         print("공중 유닛 이동")
#         self.fly(self.name, location)

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시") 

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, locaiton):
        pass    #아무처리 없이 그냥 넘어간다.

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("게임 시작")

def game_over():
    pass

game_start()
game_over()