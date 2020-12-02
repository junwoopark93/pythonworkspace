# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1],  nums[2]))
# except ValueError as verr:
#     print(verr)
# except ZeroDivisionError as err:
#     print(err)
# # except:
# #     print("알 수 없는 오류가 발생했습니다.")
# except Exception as err:
#     print(err)


# 에러 일부러 발생시키기.
# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2,  int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 수 만 입력하세요.")



# 사용자 정의 에러

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2,  int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 수 만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생했습니다. 한자리만 입력해요.")
    print(err)
finally:    #무조건 출력되는 구문.
    print("계산기를 입력해주셔서 감사합니다.")