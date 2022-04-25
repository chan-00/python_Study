# 2022.04.25일자 파이썬 공부 기록 코드

# 연산 기호 활용 계산기
'''
while True:
  num1 = int(input("첫 번째 연산할 숫자 : "));
  num2 = int(input("두 번째 연산할 숫자 : "));

  print("\n1. +\n2. -\n3. *\n4. /\n5. //\n6. %\n7. **");
  operate = input("어떤 연산자를 사용하시겠습니까?(0 입력 시 종료) : ");

  if operate == '0':
    print("0을 입력했으므로 프로그램이 종료됩니다.");
    break;
  elif operate == '+':
    result = num1 + num2;
    print(num1, '+', num2, '=', result);
  elif operate == '-':
    result = num1 - num2;
    print(num1, '-', num2, '=', result);
  elif operate == '*':
    result = num1 * num2;
    print(num1, '*', num2, '=', result);
  elif operate == '/':
    result = num1 / num2;
    print(num1, '/', num2, '=', result);
  elif operate == '//':
    result = num1 // num2;
    print(num1, '//', num2, '=', result);
  elif operate == '%':
    result = num1 % num2;
    print(num1, '%', num2, '=', result);
  elif operate == '**':
    result = num1 ** num2;
    print(num1, '**', num2, '=', result);

  print("결과값의 데이터형은 {} 입니다.".format(type(result)));
'''

# 문자열 함수 관련 코드
'''
str = "안녕하세요~, Hello World!!";
#문자열 슬라이싱
print(str[10:17]);
print(str[::-1]);
print(str[5:]);
#대문자, 소문자 변경
print(str.upper());
print(str.lower());
#문자 count
print("e 문자의 개수 : %d, ㅣ 문자의 개수 : %d, 용 문자의 개수 : %d"%(str.count('e'), str.count('l'), str.count('용')));
#문자 위치 찾기
print("World!! 문자열의 위치 찾기 : %d"%(str.find("World!!")));
#문자열 나누기
print(str.split(','));
#문자열 치환하기
print(str.replace('!!', '???'));
'''

# 입력받은 점수로 학점 출력
'''
score = int(input("점수 입력 : "));

if score >= 0 and score <= 100:
  if score >= 90:
    print("A 학점");
  elif score >= 80 and score < 90:
    print("B 학점");
  elif score >= 70 and score < 80:
    print("C 학점");
  elif score >= 60 and score < 70:
    print("D 학점");
  else:
    print("F 학점");
else:
  print("점수 입력이 똑바로 되지 않았습니다.");
'''

# random 모듈 함수 관련 문제
'''
import random

num1 = random.randint(30, 100);
num2 = random.randint(30, 100);
num3 = random.randint(30, 100);

result = (num1 + num2 + num3) / 3;

if result >= 90:
  print("{0}점, {1}점, {2}점을 받아 평균 {3}점으로 장학생입니다.".format(num1, num2, num3, result));
elif result >= 60 and result < 90:
  print("{0}점, {1}점, {2}점을 받아 평균 {3}점으로 합격입니다.".format(num1, num2, num3, result));
else:
  print("{0}점, {1}점, {2}점을 받아 평균 {3}점으로 불합격입니다.".format(num1, num2, num3, result));
'''

# 임의의 숫자만큼 별찍기
'''
num = int(input("별찍기할 숫자를 입력하세요. : "));

for i in range(1, num + 1, 1):
  print("*" * i);
print("-"*50);

for i in range(num, 0, -1):
  print("*" * i);
print("-"*50);
'''

# 임의의 숫자 구구단 출력
'''
num = int(input("구구단을 할 임의의 숫자 입력하기 : "));


for i in range(1, 10, 1):
  print(num, "X", i, "=", (num * i));

i = 1;
print();
while i <= 9:
  print(num, "X", i, "=", (num * i));
  i += 1;
'''

# 카페 문제(if문 활용)
'''
americano = 0;
cafelatte = 0;
cafuchino = 0;

print("카페");
print("-"*50);
print("아메리카노 : 3000원. 카페라떼 : 4000원, 카푸치노 : 5000원");
print("-"*50);
while True:
  input1 = int(input("아메리카노를 몇 잔 사시겠습니까?"));
  input2 = int(input("카페라떼를 몇 잔 사시겠습니까?"));
  input3 = int(input("카푸치노를 몇 잔 사시겠습니까?"));

  americano += input1;
  cafelatte += input2;
  cafuchino += input3;

  select = input("계속 주문하시겠습니까?(yes, exit)");

  if select == "exit":
    print("주문을 종료합니다.");
    break;
  elif select == "yes":
    print("주문을 이어서 받습니다.\n");
  else:
    print("문자를 잘 못 입력하였기에 주문을 계속 이어서 받겠습니다.\n");


money = int(input("지불할 금액을 입력하세요. : "));
buyMoney = (americano * 3000) + (cafelatte * 4000) + (cafuchino * 5000);

if money >= buyMoney:
  print("금액의 합 : 잔액이 %d원 만큼 남았습니다."%(money - buyMoney));
elif money < buyMoney:
  print("금액의 합 : 금액이 %d원 만큼 부족합니다."%(buyMoney - money));
'''

# 위 카페 문제에서 리스트를 활용하여 변경
'''
coffee = ["아메리카노", "카페라떼", "카푸치노"];
coffeeCount = [0, 0, 0];
coffeeMoney = [3000, 4000, 5000];

print("카페");
print("-"*50);
print("아메리카노 : 3000원. 카페라떼 : 4000원, 카푸치노 : 5000원");
print("-"*50);
while True:
  for i in range(0, 3, 1):
    coffeeCount[i] += int(input("{}를 몇 잔 사시겠습니까?".format(coffee[i])));

  select = input("계속 주문하시겠습니까?(yes, exit)");

  if select == "exit":
    print("주문을 종료합니다.");
    break;
  elif select == "yes":
    print("주문을 이어서 받습니다.\n");
  else:
    print("문자를 잘 못 입력하였기에 주문을 계속 이어서 받겠습니다.\n");


money = int(input("지불할 금액을 입력하세요. : "));
buyMoney = 0;

for i in range(0, 3, 1):
  buyMoney += (coffeeCount[i] * coffeeMoney[i]);

if money >= buyMoney:
  print("금액의 합 : 잔액이 %d원 만큼 남았습니다."%(money - buyMoney));
elif money < buyMoney:
  print("금액의 합 : 금액이 %d원 만큼 부족합니다."%(buyMoney - money));
'''

# 시작값, 끝값, 증가값 입력받아 for문 돌리며 합 계산
'''
start = int(input("시작값 : "));
end = int(input("끝값 : "));
plus = int(input("증가값 : "));
result = 0;

for i in range(start, end + 1, plus):
  result += i;

print("결과값 : {0}".format(result));
'''

# 가위바위보 문제
'''
com = ["가위", "바위", "보"];

while True:
  user = input("가위, 바위, 보 중 하나를 내시오. : ");
  comRandom = random.choice(com);

  print("\n사용자의 가위바위보 : %s"%(user));
  print("컴퓨터의 가위바위보 : %s"%(comRandom));

  if user == comRandom:
    print("비겼습니다.");
  elif (user == "가위" and comRandom == "바위") or (user == "바위" and comRandom == "보") or (user == "보" and comRandom == "가위"):
    print("컴퓨터가 이겼습니다.");
  else:
    print("사용자가 이겼습니다.");

  select = input("계속 하시겠습니까?(yes, exit) : ");

  if select == "exit":
    print("프로그램이 종료됩니다.");
    break;
  elif select == "yes":
    print("계속 입력합니다.");
'''

# 난수값 맞추기(Up, Down 출력)
'''
randomNum = random.randint(1, 50);
tryNum = 0;

while True:
  inputNum = int(input("난수값을 맞춰보시오. : "));
  tryNum += 1;

  if inputNum > randomNum:
    print("Down");
  elif inputNum < randomNum:
    print("Up");
  elif inputNum == randomNum:
    print("정답입니다!");
    break;

print("총 %d번 만에 정답을 맞췄습니다."%(tryNum));
'''

# 리스트 요소끼리 더하기
'''
list1 = [20, 340, 50];
list2 = [3.2, 90, 100.3];
listnew = list();

for i in range(0, 3, 1):
  listnew.append(list1[i] + list2[i]);

print(listnew);
'''

# 리스트에 단어 4개를 넣고 랜덤값을 뽑아 해당 값 맞추기
'''
word = ["안녕", "하세요", "제", "이름은"];
wordChoice = random.choice(word);
count = 0;

while True:
  print(word);
  wordInput = input("위 단어 중 랜덤값으로 어떤 값이 나왔는지 맞춰 보시오. : ");
  count += 1;

  if wordInput == wordChoice:
    print("정답입니다! 프로그램이 종료됩니다.");
    break;
  elif wordInput != wordChoice:
    print("오답입니다!");
  print();

print("총 {}번 만에 맞췄습니다.".format(count));
'''

# 점수를 입력받아 합격/불합격 여부와 등수 출력
'''
score = list();
rank = list();

while True:
  scoreInput = int(input("점수를 입력하시오.(음수 입력 시 종료) : "));

  if scoreInput >= 0:
    score.append(scoreInput);
    rank.append(1);
  elif scoreInput < 0:
    print("음수를 입력하였으므로 반복이 종료됩니다.");
    break;


print("\n입력된 총 점수값 ; {}".format(score));
plus = 0;

for i in range(0, len(score), 1):
  plus += score[i];

avarage = plus / len(score);
print("점수들의 합 : %d, 점수들의 평균 값 : %f"%(plus, avarage));
human = 0;

print();
for i in range(0, len(score), 1):
  for j in range(0, len(score), 1):
    if score[i] < score[j]:
      rank[i] += 1;

  if score[i] >= 70:
    print("{} 번째 학생은 합격입니다.(등수 : {})".format(i + 1, rank[i]));
    human += 1;
  elif score[i] < 70:
    print("{} 번째 학생은 불합격입니다.(등수 : {})".format(i + 1, rank[i]));

print("\n총 합격자 수는 %d 명입니다."%(human));
'''

# 테스트용 난수 2개의 덧셈 결과 맞추기
'''
score = 0;
tryNum = 0;

while True:
  randNum1 = random.randint(1, 10);
  randNum2 = random.randint(1, 10);

  print("테스트용 난수 : %d, %d"%(randNum1, randNum2));
  result = int(input("난수들의 덧셈 결과값 입력(0 입력 시 종료) : "));

  if result == (randNum1 + randNum2):
    print("정답입니다!");
    score += 10;
  elif result == 0:
    print("0을 입력했으므로 프로그램을 종료합니다.");
    break;
  
  tryNum += 1;
  

print("\n점수 : %d"%(score));
print("정답 확률은? %d번 시도, %d번 정답 : %.2f%%"%(tryNum, (score // 10), ((score // 10)/tryNum)*100));
'''

# 임의의 숫자 입력받아 10으로 나눈 몫만큼 특수문자 출력
'''
while True:
  num = int(input("임의의 숫자 입력(0 입력 시 종료) : "));

  if num == 0:
    print("0을 입력했으므로 프로그램을 종료합니다.");
    break;
  elif num != 0:
    print("★"*(num//10));
'''