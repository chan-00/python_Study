import random

comlst = [0, 0, 0];
com1, com2 = 0, 0;
lst = ["가위", "바위", "보"];
count = 0;
# 홍길동과 김말동의 가위바위보 전적값
comlst1 = [0, 0, 0];
comlst2 = [0, 0, 0];
#Draw Report 값
drawlst = [0, 0, 0];

print("\t홍길동 vs 김말동 가위바위보 게임 ==");
select = int(input("[1] 세부내용 보기, [2] 결과만 보기 : "));
number = int(input("가위바위보 게임 몇회 할까요? : "));

# 1 : 세부내용 보기, 2 : 결과만 보기의 선택 결과에 따라 조건식으로 나눠 1에서는 세부내용 출력.
if select == 1:
  print("홍길동\t김말동\t결과");
  print("-" * 21);

  while count < number:
    com1 = random.randint(1, 3);
    com2 = random.randint(1, 3);
    print("%s\t%s"%(lst[com1 - 1], lst[com2 - 1]), end='');

    if com1 == com2:
      print("\tDraw");
      comlst[1] += 1;
      #drawlst 값 계산
      if com1 == 1:
        drawlst[0] += 1;
      elif com1 == 2:
        drawlst[1] += 1;
      elif com1 == 3:
        drawlst[2] += 1;
    elif com1 + 1 == com2 == 2 or com1 + 1 == com2 == 3 or (com1 == 3 and com2 == 1):
      comlst[2] += 1;
      #김말동의 가위바위보 전적 계산
      if com2 - 1 == 0:
        comlst2[0] += 1;
      elif com2 - 1 == 1:
        comlst2[1] += 1;
      elif com2 - 1 == 2:
        comlst2[2] += 1;
      print("\t김말동Win");
    else:
      comlst[0] += 1;
      #홍길동의 가위바위보 전적 계산
      if com1 - 1 == 0:
        comlst1[0] += 1;
      elif com1 - 1 == 1:
        comlst1[1] += 1;
      elif com1 - 1 == 2:
        comlst1[2] += 1;
      print("\t홍길동Win");

    count += 1;
elif select == 2:
  while count < number:
    com1 = random.randint(1, 3);
    com2 = random.randint(1, 3);

    if com1 == com2:
      comlst[1] += 1;
      #drawlst 값 계산
      if com1 == 1:
        drawlst[0] += 1;
      elif com1 == 2:
        drawlst[1] += 1;
      elif com1 == 3:
        drawlst[2] += 1;
    elif com1 + 1 == com2 == 2 or com1 + 1 == com2 == 3 or (com1 == 3 and com2 == 1):
      comlst[2] += 1;
      #김말동의 가위바위보 전적 계산
      if com2 - 1 == 0:
        comlst2[0] += 1;
      elif com2 - 1 == 1:
        comlst2[1] += 1;
      elif com2 - 1 == 2:
        comlst2[2] += 1;
    else:
      comlst[0] += 1;
      #홍길동의 가위바위보 전적 계산
      if com1 - 1 == 0:
        comlst1[0] += 1;
      elif com1 - 1 == 1:
        comlst1[1] += 1;
      elif com1 - 1 == 2:
        comlst1[2] += 1;

    count += 1;

# 총 비긴 횟수값
drawSum = drawlst[0] + drawlst[1] + drawlst[2];

#홍길동과 김말동의 가위바위보 추천값 작성
maxLst1, maxLst2 = max(comlst1), max(comlst2);
maxComLst1, maxComLst2 = [], [];

for i in range(0, 3):
  if maxLst1 == comlst1[i]:
    if i == 0:
      maxComLst1.append("가위");
    elif i == 1:
      maxComLst1.append("바위");
    elif i == 2:
      maxComLst1.append("보");
  if maxLst2 == comlst2[i]:
    if i == 0:
      maxComLst2.append("가위");
    elif i == 1:
      maxComLst2.append("바위");
    elif i == 2:
      maxComLst2.append("보");

# 홍길동과 김말동의 각 승률 출력
print("-" * 55);
print("\t홍길동승률: %.2f%% [%d승%d무%d패]"%((comlst[0]/count*100), comlst[0], comlst[1], comlst[2]));
print("\t김말동승률: %.2f%% [%d승%d무%d패]"%((comlst[2]/count*100), comlst[2], comlst[1], comlst[0]));
print("\t Draw확률 : %.2f%%"%(comlst[1]/count*100));
print("-" * 55);
print("\n");

#REPORT 부분 출력
print("\t\tR E P O R T");
print("=" * 55);
#홍길동 Report
print("\t\t홍길동 Report[\t%d( %.2f%%)]"%(comlst[0], (comlst[0]/count*100)));
print("-" * 55);
print("\t가위\t\t바위\t\t보");
print("\t%d( %.2f%%)\t%d( %.2f%%)\t%d( %.2f%%)"%(comlst1[0], (comlst1[0]/count*100), comlst1[1], (comlst1[1]/count*100), comlst1[2], (comlst1[2]/count*100)));
print("-" * 55);
#김말동 Report
print("\t\t김말동 Report[\t%d( %.2f%%)]"%(comlst[2], (comlst[2]/count*100)));
print("-" * 55);
print("\t가위\t\t바위\t\t보");
print("\t%d( %.2f%%)\t%d( %.2f%%)\t%d( %.2f%%)"%(comlst2[0], (comlst2[0]/count*100), comlst2[1], (comlst2[1]/count*100), comlst2[2], (comlst2[2]/count*100)));
print("-" * 55);
#DRAW Report
print("\t\tDRAW Report[\t%d( %.2f%%)]"%(drawSum, (drawSum/count*100)));
print("\t가위\t\t바위\t\t보");
print("\t%d( %.2f%%)\t%d( %.2f%%)\t%d( %.2f%%)"%(drawlst[0], (drawlst[0]/count*100), drawlst[1], (drawlst[1]/count*100), drawlst[2], (drawlst[2]/count*100)));
print("-" * 55);
#가위바위보 추천
print("홍길동을 위한 추천 :\t{}".format(maxComLst1));
print("김말동을 위한 추천 :\t{}".format(maxComLst2));
print("=" * 55);