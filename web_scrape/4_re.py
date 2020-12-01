#정규식 예제
import re

#abcd, book, desk
#ca?e
#care, cafe, case, cave
# caae, cabe, cace, cade, ....

p = re.compile("ca.e")
# . 하나의 문자 의미 > care, cafe, case
# ^de : 문자열의 시작 > desk, destination
# $ (se$) : 문자열의끝 > case, base


def print_match(m):
    if m:
        print("m.group():", m.group())    #group 매치가 되었는지 확인할 때
        print("m.string:", m.string)
        print("m.start():", m.start())
        print("m.end():", m.end())
        print("m.span():", m.span())
    else:
        print("매칭되지 않음")

# m = p.match("careless") #match : 주어진 문자열의 처움부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe cave") # findall : 일치하는 모든 것을 리스트 형태로 변환
print(lst)


# 사용 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는 지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는지 확인
# 3. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리슽" 형태로 반환

# . 하나의 문자 의미 > care, cafe, case
# ^de : 문자열의 시작 > desk, destination
# $ (se$) : 문자열의끝 > case, base