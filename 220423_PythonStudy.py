#가위바위보 10번 회전
'''
import random

com1, com2 = 0, 0;
count = 0;
comlst = [0, 0, 0];
lst = ["가위", "바위", "보"];

print("com1\tcom2\tresult");
print("-" * 21);

while count < 10:
  com1 = random.randint(1, 3);
  com2 = random.randint(1, 3);
  print("%s\t%s"%(lst[com1 - 1], lst[com2 - 1]), end='');

  if com1 == com2:
    print("\tDraw");
    comlst[1] += 1;
  elif com1 + 1 == com2 == 2 or com1 + 1 == com2 == 3 or (com1 == 3 and com2 == 1):
    comlst[2] += 1;
    print("\t\in -> com2 [%d승%d무%d패]"%(comlst[2], comlst[1], comlst[0]));
  else:
    comlst[0] += 1;
    print("\t\in -> com1 [%d승%d무%d패]"%(comlst[0], comlst[1], comlst[2]));

  count += 1;

print("-"*21);
print("com1이 이길 확률 : %d%%"%(comlst[0]/count*100));
print("com2가 이길 확률 : %d%%"%(comlst[2]/count*100));
print("비길확률 : %d퍼센트"%(comlst[1]/count*100));
'''