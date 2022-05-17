#220517 파이썬 공부 기록

#함수 예제01
'''
def sumFunc():
  num1 = int(input("정수1 ==> "));
  num2 = int(input("정수2 ==> "));
  return num1 + num2;

listName = ['A', 'B', 'C'];

for i in listName:
  print("%s님, 두 숫자를 입력하세요."%(i));
  sum = sumFunc();
  print("결과 : %d"%(sum));

'''

#함수 예제02(계산기)
'''
def calc(v1, v2, op) :
  result = 0;
  if op == '+':
    result = v1 + v2;
  elif op == '-':
    result = v1 - v2;
  elif op == '*':
    result = v1 * v2;
  elif op == '/':
    result = v1 / v2;
  else:
    result = -9999999;
  return result;

operate = input("계산 입력(+, -, *, /) : ");
var1 = int(input("첫 번째 숫자 : "));
var2 = int(input("두 번째 숫자 : "));
result = calc(var1, var2, operate);

if result == -9999999:
  print("연산자 입력이 잘못 되었습니다.");
else:
  print("계산 결과 : {0} {1} {2} = {3:0.2f}".format(var1, operate, var2, result));
'''

#함수 예제03
'''
def plus(v1, v2):
  return v1 + v2;

def minus(v1, v2):
  return v1 - v2;

def multi(v1, v2):
  return v1 * v2;

def div(v1, v2):
  return v1 / v2;

while True:
  res = 0;
  oper = input("계산 입력(+, -, *, /) : ");
  var1 = int(input("첫 번째 숫자 : "));
  var2 = int(input("두 번째 숫자 : "));

  if oper == '+':
    res = plus(var1, var2);
  elif oper == '-':
    res = minus(var1, var2);
  elif oper == '*':
    res = multi(var1, var2);
  elif oper == '/':
    res = div(var1, var2);
  else:
    print("연산자를 잘못 입력했으므로 프로그램이 종료됩니다.");
    break;
  print("결과 : %d %s %d = %.2f\n"%(var1, oper, var2, res));
'''

#함수 예제04(매개변수의 활용)
'''
# 매개변수의 디폴트값 지정 가능
def para_func(v1, v2 = 0, v3 = 0):
  return v1 + v2 + v3;

# 여러 값을 b에 모두 받을 수 있음
# * 표시로 여러 값을 받는 것은 마지막 매개변수에만 가능
def test(a, *b):
  print(a, b);

# 리스트도 매개변수로 주고받기 가능
def list_func(lst):
  sum = 0;
  print("list 내용 : ", end='');
  for i in range(1, len(lst), 2):
    print(lst[i], end=' ');
    sum += lst[i];
  print();
  return sum;

res = para_func(10, 20);
print("res =", res);
res = para_func(10);
print("res =", res);
print();

test(1, 2, 3);
print();

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
sum = list_func(list1);
print("합계 : %d"%(sum));
print();
'''

#튜플 활용하여 매개변수 받기
'''
def para_func(*para):
  sum = 0;
  for i in para:
    sum += i;
  return sum;

sum = para_func(10, 20, 30);
print("세 수의 합 :", sum);
sum = para_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
print("1 ~ 10까지의 합 :", sum);
'''

#딕셔너리 매개변수로 받기
'''
def dic_func(**para):
  res = 0;
  for k in para.keys():
    print("%s -> %d 명입니다."%(k, para[k]));
    res += para[k];
  return res;

sum = dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4);
print("인원의 합 : %d"%(sum));
'''

#함수의 여러 유형
'''
def test1():
  print("반환값 없음");

def test2(a):
  print(a, "반환값 없음, 매개변수 있음");

def test3(x, y):
  return x + y;

def test4(x, y):
  return x + y, x - y, x * y, x / y;

test1();
print();
test2(5);
print();
print("매개변수와 반환값 모두 있음 :", test3(1, 2));
print();

print("반환값이 여러 개인 경우");
a, b, c, d = test4(7, 5);
print(a, b, c, d);
print();
'''

#함수 예제05(리스트 활용 함수)
'''
def price(strMenu):
  lst = [1200, 1800, 2500, 1500];
  if strMenu == "아메리카노":
    print(strMenu, "가격 :", lst[0]);
  elif strMenu == "카페라떼":
    print(strMenu, "가격 :", lst[1]);
  elif strMenu == "바닐라라떼":
    print(strMenu, "가격 :", lst[2]);
  elif strMenu == "홍차":
    print(strMenu, "가격 :", lst[3]);

menuList = ["아메리카노", "카페라떼", "바닐라라떼", "홍차"];
menu = int(input("메뉴 선택(1. 아메리카노, 2. 카페라떼, 3. 바닐라라떼, 4. 홍차 : "));
if menu >= 1 and menu <= 4:
  price(menuList[menu-1]);
else:
  print("메뉴값을 잘못 입력했습니다.");
'''

#함수 예제06(리스트 활용 패턴인식 문제)
'''
def patternmatch(pt):
  for i in range(0, len(pt)-1, 1):
    print(pt[i], end=',');
  print('\b');
  userinp = int(input("다음 입력값? "));

  if userinp == pt[len(pt)-1]:
    print("맞습니다.\n");
    return "정답";
  else:
    print("틀립니다.\n");
    return "오답";

pattern = [[1, 2, 3, 4, 5], [2, 4, 6, 8], [1, 1, 2, 3, 5, 8]];
wrong = 0;
correct = 0;

for i in pattern:
  result = patternmatch(i);

  if result == "정답":
    correct += 1;
  elif result == "오답":
    wrong += 1;
  
print("%d번 중 %d번 맞았습니다."%(correct+wrong, correct));
'''