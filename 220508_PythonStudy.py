#재귀 함수(순회 함수)의 끝나는 조건 => 인덱스(i)가 주어진 배열의 길이를 넘었을 때
#각 순회 함수 종류에 따라 출력(print)의 위치가 다른 것을 확인할 수 있습니다.

#전위 순회 함수
def preorder(exTree, i):
    if i >= len(exTree):
        return
    if exTree[i] != 0:
        print(exTree[i], end=' ')
        preorder(exTree, i*2)
        preorder(exTree, (i*2)+1)
#중위 순회 함수
def inorder(exTree, i):
    if i >= len(exTree):
        return
    if exTree[i] != 0:
        inorder(exTree, i*2)
        print(exTree[i], end=' ')
        inorder(exTree, (i*2)+1)
#후위 순회 함수
def postorder(exTree, i):
    if i >= len(exTree):
        return
    if exTree[i] != 0:
        postorder(exTree, i*2)
        postorder(exTree, (i*2)+1)
        print(exTree[i], end=' ')

#예시 리스트(트리 표현)
exTree = [7, 'A', 'B', 'C', 'D', 0, 'E', 'F', 0, 0, 0, 0, 0, 0, 0, 'G', 0]

#순회 함수 호출
print("<트리 전위 순회>")
preorder(exTree, 1)
print("\n<트리 중위 순회>")
inorder(exTree, 1)
print("\n<트리 후위 순회>")
postorder(exTree, 1)