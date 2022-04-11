#220411_학교 python_Study

# 리스트, random 모듈 활용 문제
'''
import random

word = ['사과', '포도', '빨간색'];
w = random.choice(word);

while True:
  print(word);
  str = input("\n위 리스트 중 랜덤값으로 나온 값을 맞추시오. : ");

  if w == str:
    print("맞췄습니다! 반복문을 빠져 나갑니다.");
    break;
  elif w != str:
    print("맞추지 못했습니다. 이어서 입력합니다.");
  else:
    print("위의 리스트에 없는 값을 입력했으므로 다시 입력을 받습니다.");

print("랜덤으로 뽑힌 값 : %s, 입력한 값 : %s"%(w, str));
print("프로그램 종료.");
'''

# random모듈 활용 문제
'''
import random

num1 = random.randint(1, 100);
num2 = random.randint(1, 100);

while True:
  inpNum = int(input("%d + %d = "%(num1, num2)));

  if inpNum == (num1 + num2):
    print("정답입니다!");
    break;
  elif inpNum != (num1 + num2):
    print("정답이 아닙니다.");

print("프로그램 종료.");
'''

# 리스트 활용 문제
'''
numList = list();
rank = list();
sum = 0;
passHuman = 0;

while True:
  inpNum = int(input("점수 입력 : "));

  if(inpNum >= 0):
    numList.append(inpNum);
    rank.append(1);
    sum += inpNum;
  elif(inpNum < 0):
    print("음수를 입력했으므로 반복을 빠져나갑니다.\n");
    break;

print("입력한 사람들의 점수 출력 = ", end='');
print(numList);
avg = float(sum) / len(numList);
print("점수들의 합 : %d, 점수의 평균 : %f\n"%(sum, avg));

for i in range(0, len(numList), 1):
  for j in range(0, len(rank), 1):
    if numList[i] < numList[j]:
      rank[i] += 1;


  if(numList[i] >= 70):
    print("%d번째 사람은 %d점이므로 합격입니다.(%d등)"%((i + 1), numList[i], rank[i]));
    passHuman += 1;
  else:
    print("%d번째 사람은 %d점이므로 불합격입니다.(%d등)"%((i + 1), numList[i], rank[i]));

print("\n총 합격자 수는 %d명입니다."%(passHuman));
'''

# 2차원 리스트 문제
'''
student = [];
sum = 0;
num = int(input("학생수? "));
for i in range(num):
  print("학생 정보 입력 : >>");
  name = input("이름 ? ");
  score = int(input("%s의 점수? "%(name)));
  student.append([name, score]);
  sum += score;

searchName = input("검색할 이름을 입력하시오 ");

for lst in student:
  if lst[0] == searchName:
    print("이름 : %s, 점수 : %d"%(lst[0], lst[1]));

print("평균 = %.2f"%(sum/num));
'''