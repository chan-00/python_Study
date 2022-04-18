# 2022.04.18일자 학교 강의(파이썬) 공부
'''
# 랜덤함수 사용 문제01
import random

score = 0;
tryNum = 0;

while True:
    a = random.randint(1, 10);
    b = random.randint(1, 10);
    result = a + b;

    print("테스트용 난수 보이기 : %d, %d" % (a, b));
    numInp = int(input("임의의 두 수의 덧셈 결과는?(종료 0) : "));

    if numInp == 0:
        print("0을 입력했으므로 프로그램이 종료됩니다.");
        break;
    elif numInp == result:
        print("정답입니다!");
        score += 10;
    elif numInp != result:
        print("정답이 아닙니다.");

    print();
    tryNum += 1;

print("최종 점수 : %d" % (score));
print("정답 확률은? %d번 시도, %d번 정답 => %.2f%%" % (tryNum, score // 10, ((score // 10) / tryNum) * 100));
'''

'''
# 연산자 사용 문제02
while True:
  numInp = int(input("임의의 숫자 입력(0 종료) : "));

  if numInp == 0:
    print("프로그램이 종료됩니다.");
    break;
  elif numInp > 0:
    for n in range(0, (numInp//10), 1):
      print("■", end='');
  else:
    print("숫자를 똑바로 입력하세요.");

  print();
'''