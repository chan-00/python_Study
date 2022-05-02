#2차원 리스트
'''
alist = [1, 2, 3, 4, 5];      #1차원 리스트
blist = [[1, 2, 3, 4], [5, 6, 7], [9, 10, 11, 12, 13]];      #2차원 리스트(3행 4열)

print("<1차원 리스트 출력>");
for i in range(len(alist)):
  print(alist[i], end=' ');
print();

print("\n<2차원 리스트 출력01>");
for i in range(len(blist)):
  for j in range(len(blist[i])):
    print(blist[i][j], end=' ');
  print();

print("\n<2차원 리스트 출력02>");
for i in blist:
  for j in i:
    print(j, end=' ');
  print();
'''

#2차원 리스트 응용 문제
'''
import random
human = [];

for i in range(5):
  line = [];
  name = input("성명 : ");                      #이름 입력
  studNum = random.randint(21100, 21200);       #학번 랜덤값
  kor = random.randint(55, 99);                 #국어 랜덤값
  eng = random.randint(55, 99);                 #영어 랜덤값
  math = random.randint(55, 99);                #수학 랜덤값
  sum = kor + eng + math;                       #총점 계산
  avg = sum / 3;                                #평균 계산
  #리스트에 값 넣기
  human.append([studNum, name, kor, eng, math, sum, avg, 1]);

print("="*60);
print("학번\t성명\t국어\t영어\t수학\t총점\t평균\t등수");
print("="*60);

#등수 계산 및 전체 출력
for i in range(len(human)):
  for j in range(len(human)):
    if human[i][6] < human[j][6]:
      human[i][7] += 1;
  print(human[i]);

#학번 검색
searchNum = int(input("검색할 학번? "));
searchBool = False;

#검색한 학번의 내용이 있는지 판단하여 출력
for i in range(len(human)):
  if human[i][0] == searchNum:
    print("="*60);
    print("학번\t성명\t국어\t영어\t수학\t총점\t평균\t등수");
    print("="*60);
    print(human[i]);
    searchBool = True;

if searchBool == False:
  print("검색한 학번의 정보가 존재하지 않습니다.");
'''

#그래프 라이브러리들
'''
import matplotlib.pyplot as plt
import pandas as pd

plt.plot([1, 2, 3, 4, 5], [60, 50, 40, 70, 50]);            #선그래프
plt.plot([1, 2, 3, 4, 5], [60, 50, 40, 70, 50], 'ro');      #점그래프
plt.bar([1, 2, 3, 4], [1, 6, 5, 10]);                       #막대그래프
'''
'''
import pandas as pd

mlist = [10, 20, 30, 40, 50];
pd.Series(mlist);
'''
'''
import pandas as pd
df1 = pd.DataFrame([[20, '소프트웨어과', '2학년', '남'], 
                    [22, '소프트웨어과', '2학년', '남'], 
                    [21, '멀티미디어과', '1학년', '여']], 
                   index=['영호', '준호', '민호'],
                   columns=['나이', '학과', '학년', '성별']);
print(df1);
'''
'''
import pandas as pd
html_file = 'https://www.daishin.com/g.ds?m=88&p=3647&v=2694';
d3 = pd.read_html(html_file);
print(d3);
'''

#튜플
'''
t1 = (1, 2, 3, 4, 5)        #튜플
t2 = 10, 20, 30, 40, 50     #튜플
print(t1);
print(t2);
'''
'''
#리스트와 튜플 사이에 형변환 가능
#리스트로 형변환하여 인덱스값의 변경 후 튜플로 재형변환한 예제
t1 = (1, 2, 3, 4, 5);
list1 = list(t1);
list1.append(6);
t1 = tuple(list1);
print(t1);
'''

#딕셔너리
'''
aset = {1, 2, 3, 4, 5};
bset = {3, 4, 5, 6, 7, 8};
print(aset, bset);
print(aset & bset);         #교집합
print(aset.intersection(bset));
print(aset | bset)           #합집합
print(aset.union(bset));
print(aset - bset)           #차집합
print(aset.difference(bset));
'''