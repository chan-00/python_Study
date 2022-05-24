# 2차원 리스트 활용 함수 예제01
'''
def list_func(lst_2):
  for lst in lst_2:
    sum = 0;
    for k in lst:
      if str(type(k)) == "<class 'int'>":
        sum += k;
        print("%3d\t"%(k), end="");
      else:
        print("%s\t"%(k), end="");
    print("%3d"%sum);

list1 = ["홍길동", 90, 90, 90];
list2 = ["김말동", 98, 98, 88];
list3 = ["이기자", 78, 77, 65];
list4 = [];

list4.append(list1);
list4.append(list2);
list4.append(list3);
print('-'*40);
print(" 성명\t국어\t영어\t수학\t총점");
print('-'*40);
list_func(list4);
print('-'*40);
'''

# 예제 문제02(id 입력받아 판단)
'''
def idCheck(id, lenID):
  if id.isalnum() and lenID >= 8:
    return True;
  else:
    return False;

for i in range(3):
  id = input("id? ");
  access = idCheck(id, len(id));

  if access:
    print("입장 가능");
  else:
    print("입장 불가능");
'''

# 로또 번호출력 문제03
'''
import random

def lotto():
  lst = [];

  while True:
    r = random.randint(1, 46);
    if r not in lst:
      lst.append(r);
    if len(lst) == 6:
      break;

  return lst;

lot = lotto();
print(lot);
'''

# 지역변수, 전역변수 예제
'''
# 함수 정의
def func1():
  n1 = 10
  print("func1()에서 n1 : %d / n2 : %d" % (n1, n2))
def func2():
  n2 = 100
  print("func2( )에서 n1 : %d / n2 : %d" % (n1, n2))
# 전역변수
n1 , n2 = 20 , 200
# 함수 사용
func1( )
func2( )
'''

# 내부함수 예제
'''
def outfun(v1, v2):
  def infun(num1, num2):
    return num1+num2
  def minus(num1, num2):
    return num1-num2
  return infun(v1, v2), minus(v1, v2)

print(outfun(5,3))
'''

# 재귀함수 문제(팩토리얼)
'''
def factorial(num):
  if num == 1:
    return 1;
  return num * factorial(num - 1);

print(factorial(5));
print(factorial(8));
'''