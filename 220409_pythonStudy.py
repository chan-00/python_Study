# 리스트 활용
'''
menu = ["아메리카노", "카페라떼", "카푸치노"];
price = [3000, 4000, 5000];
sum = 0;

print("**카페**");
print("-" * 55);
print("메뉴 : 아메리카노(3000), 카페라떼(4000), 카푸치노(5000)");
print("-" * 55);

while True:
  for i in range(0, len(menu)):
    inputCoffee = int(input("%s 갯수? "%(menu[i])));
    sum += (inputCoffee * price[i]);

  select = input("계속 주문하시겠습니까?(yes or exit) ");

  if select == "yes":
    continue;
  elif select == "exit":
    print("지불 금액을 입력합니다.");
  else:
    print("yes 또는 exit를 입력하지 않았으므로 프로그램이 종료됩니다.");
    break;

  money = int(input("지불금액? "));

  if money - sum > 0:
    print("금액의 합 : %d원으로 거스름돈 %d원"%(sum, (money - sum)));
  elif money - sum < 0:
    print("금액의 합 : %d원으로 금액부족"%(sum));

  break;
'''

# random 모듈 사용해보기
'''
import random         #random 모듈 불러오기
a = random.random()   #0.0 ~ 0.9999 사이의 실수
print(a);
a = random.uniform(10, 20);
print(a);
a = random.randint(10, 20);
print(a);
a = random.randrange(10, 20);
print(a);
a = random.choice(["사과", "배", "복숭아"]);
print(a);
a = random.sample(range(1, 46), 6);
print(a);
'''

# 1~50 난수 맞추기
'''
import random

correct = 0;
comNum = random.randint(1, 50);

while True:
  inp = int(input("난수를 맞춰보세요. : "));

  correct += 1;

  if inp > comNum:
    print("난수보다 큽니다.");
  elif inp < comNum:
    print("난수보다 작습니다.");
  elif inp == comNum:
    print("맞췄습니다!");
    break;

print("\n%d번만에 맞췄습니다."%(correct));
print("컴퓨터의 난수는 %d였습니다."%(comNum));
print("프로그램이 종료됩니다.");
'''