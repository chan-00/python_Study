#반환값에 따른 함수의 동작 살펴보기
'''
#반환값 없는 함수
def noFunc():
  print("반환값이 없는 함수입니다.")
  return

#반환값 1개인 함수
def oneFunc():
  print("반환값이 1개인 함수입니다.")
  sum = 0
  for i in range(1, 11):
    sum+=i
  return sum

#반환값이 2개 이상인 함수
def twoFunc():
  print("반환값이 2개 이상인 함수입니다.")
  one, two, three = 1, 2, 3
  return one, two, three

noFunc()
print(oneFunc())
#반환값이 2개 이상일 경우 해당 반환값 수에 맞게 받는 변수의 개수도 같아야 한다.
one, two, three = twoFunc()

print(one, two, three)
'''

#지역변수와 전역변수 차이 알아보는 예제(global 키워드도 사용)
'''
def func1():
  num1 = 20
  print("num1 =", num1, ", num2 =", num2)

def func2():
  num2 = 40
  print("num1 =", num1, ", num2 =", num2)

def func3():
  global num1
  num1 = 100
  print("num1 =", num1, ", num2 =", num2)

num1 = 10
num2 = 30

func2()
func3()
func1()
'''

#함수에서 매개변수로 리스트, 튜플, 딕셔너리를 받아서 처리하는 예제 만들기
'''
#매개변수 리스트 처리
def lstFunc(lst):
  for i in lst:
    for j in i:
      print(j, end=' ')
    print()

#매개변수 튜플 처리
def tupfunc(*para):
  sum = 0
  for i in para:
    sum += i
  return sum

#매개변수 딕셔너리 처리
def dicFunc(**dic):
  for key in dic.keys():
    print(key,"=",dic[key])


lstFunc([[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11, 12, 13]])
sum = tupFunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dicFunc(첫번째 = 1, 두번째 = 2, 세번째 = 3, 네번째 = 4)
print(sum)
'''

#두 실수를 입력받아 사칙연산 결과 4개를 한꺼번에 반환하는 함수를 포함하는 코드 작성
'''
def calc(v1, v2):
  sum = v1 + v2
  minus = v1 - v2
  multi = v1 * v2
  div = v1 / v2
  return sum, minus, multi, div

sum, minus, multi, div = calc(6, 3)
print(sum, minus, multi, div)
'''

#내부함수를 활용하여 계산기 함수 안에 계산하는 함수 4개(+, -, *, /)를 만들기
'''
def calc(v1, v2):
  def sum(v1, v2):
    return v1 + v2
  def minus(v1, v2):
    return v1 - v2
  def multi(v1, v2):
    return v1 * v2
  def div(v1, v2):
    return v1 / v2
  return sum(v1, v2), minus(v1, v2), multi(v1, v2), div(v1, v2)

num1, num2, num3, num4 = calc(10, 5)
print(num1, num2, num3, num4)
'''

#두 매개변수의 덧셈값을 반환하는 람다 함수를 만들어 보기
'''
sum = lambda v1, v2 : v1 + v2
print(sum(1, 1))
'''

#재귀함수 활용 팩토리얼 함수 만들기
'''
def facto(v1):
  if v1 == 1:
    return 1
  return v1 * facto(v1 - 1)

print(facto(4))
'''

#규칙에 맞게 비밀번호를 작성하도록 하는 함수 작성하기 (8글자 이상, 영문자 및 숫자로만 생성해야 하면 기호는 불가능)
'''
def checkPass(passStr):
  if passStr.isalnum() and len(passStr) >= 8:
    return True
  else:
    return False

while True:
  passStr = input("새로운 비밀번호를 입력하세요 : ")
  if checkPass(passStr):
    print("Good~ 비밀번호가 올바르게 생성되었어요")
    break;
  else:
    print("오류! 비밀번호가 규칙에 맞지 않습니다.")
'''

#output.txt라는 파일에 문자열을 작성하고, 파일 읽기로 output 파일의 내용을 읽어오는 예제 만들기
'''
try:
  wfile = open("output.txt", "w")
  while True:
    istr = input("파일에 쓸 문자열을 입력하세요(엔터키 입력 시 종료) : ")
    if istr == "":
      break
    else:
      wfile.writelines(istr+"\n")

  print("output.txt 파일에 위의 내용들이 저장되었습니다.")
  wfile.close()

  rfile = open("output.txt", "r", encoding="UTF-8")
  lst = rfile.readlines()
  for i in lst:
    print(i, end='')
except:
  print("오류가 났습니다.")
'''