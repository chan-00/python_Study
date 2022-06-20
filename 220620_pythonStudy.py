#입력한 id, 비밀번호 체크
'''
def idCheck(id):
  if len(id) <= 8:
    return True
  else:
    return False

def passCheck(pw):
  if len(pw) <= 8 and pw.isalnum():
    return True
  else:
    return False

id = input("아이디를 입력하세요. : ")
pw = input("비밀번호를 입력하세요. : ")

if idCheck(id) and passCheck(pw):
  print("Good, 입장하세요.")
else:
  print("다시 입력하세요")
'''

#점수 입력받아 합계와 평균 계산 함수
'''
def sum(lst):
  s = 0
  for i in lst:
    s = s + i
  return s

def avg(lst):
  count = 0
  s = 0
  for i in lst:
    if i != 0:
      s = s + i
      count = count + 1
  return s / count

score = []

while True:
  iscore = int(input("점수는? "))
  score.append(iscore)
  if iscore == 0:
    break

print(score)
print("합계 =", sum(score))
print("평균 = %.2f"%avg(score))
'''