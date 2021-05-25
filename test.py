import os
import random

class clear():                          #화면 초기화 클래스
  def clr():
    os.system('cls')

class Node(object):                     #클래스 정의 및 초기화하기
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

class BinarySearchTree(object):
  def __init__(self):                   #빈 트리로 초기화
    self.root = None


  def insert(self, data):               #원소 저장
    self.root = self._insert_value(self.root, data)
    return self.root is not None
  def _insert_value(self, node, data):
    if node is None:
      node = Node(data)
    else:
      if data <= node.data:
        node.left = self._insert_value(node.left, data)
      else:
        node.right = self._insert_value(node.right, data)
    return node

  
  def find(self, key):                    #원소 찾기
    return self._find_value(self.root, key)

  def _find_value(self, root, key):
    if root is None or root.data == key:
      return root is not None
    elif key < root.data:
      return self._find_value(root.left, key)
    else:
      return self._find_value(root.right, key)

  
  def delete(self, key):                 #원소 지우기
    self.root, deleted = self._delete_value(self.root, key)
    return deleted

  def _delete_value(self, node, key):
    if node is None:
      return node, False
    
    deleted = False
    if key == node.data:
      deleted = True
      if node.left and node.right:              #만약 자손 둘다 지웟을 경우 오른쪽에 있는 노드에 있는 원소 중에 맨 왼쪽에 있는 노드로 교체합니다.
        parent, child = node, node.right
        while child.left is not None:
          parent, child = child, child.left
        child.left = node.left
        if parent != node:
          parent.left = child.right
          child.right = node.right
        node = child
      elif node.left or node.right:
        node = node.left or node.right
      else:
        node = None
    elif key < node.data:
        node.left, deleted = self._delete_value(node.left, key)
    else:
      node.right, deleted = self._delete_value(node.right, key)
    return node, deleted
  def level_order_traversal(self):              #큐를 사용하여 레벨 순회 알고리즘 사용
    def _level_order_traversal(root):
        queue = [root]
        while queue:
            root = queue.pop(0)
            if root is not None:
                print(root.data)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
    _level_order_traversal(self.root)


array = [random.randint(30,70)]
bst = BinarySearchTree()
for x in array:
  bst.insert(x)
while True:                                                         #while문이 True일때까지 반복
  clear.clr()                                                       #화면 초기화
  print("-"*30)
  print("3의 배수 숫자 10개이상 뽑기")
  print("-"*30)
  print("\n\n")
  print("1. 시작하기\n2. 종료하기")
  print("\n\n")
  while True:                                                       #while문이 True일때까지 반복
    try:                                                            #예외처리 try와 except를 사용하여 숫자가 아닌 다른 형식의 원소를 받앗을때 다시 입력하도록 만듬
      game = int(input("시작하시겟습니까?"))
      break
    except ValueError:
      clear.clr()
      print("-"*30)
      print("3의 배수 숫자 10개이상 뽑기")
      print("-"*30)
      print("\n\n")
      print("1. 시작하기\n2. 종료하기")
      print("\n\n")
  if(game == 1):
    clear.clr()
    while True:
      count = 0                                                     #3의 배수의 갯수 확인을 위한 변수
      con = 0                                                       #숫자 10개 이상일때 줄바꿈하기 위한 변수
      print("="*30)
      print("1. 숫자 뽑기\n2. 특정 숫자 지우기\n3. 특정 숫자 여부 확인\n4. 채점하기(전체 숫자 보기)\n5. 레벨순회로 표기\n6. 초기화면으로 넘어가기")
      print("="*30)
      while True:
        try:                                                         #예외처리 try와 except를 사용하여 숫자가 아닌 다른 형식의 원소를 받앗을때 다시 입력하도록 만듬
          menu = int(input("원하시는 항목을 선택해 주세요 : "))
          break
        except ValueError:
          clear.clr()
          print("="*30)
          print("1. 숫자 뽑기\n2. 특정 숫자 지우기\n3. 특정 숫자 여부 확인\n4. 채점하기(전체 숫자 보기)\n5. 레벨순회로 표기\n6. 초기화면으로 넘어가기")
          print("="*30)
          print("다시 작성해주세요")

      if(menu<=6):
        clear.clr()
        if(menu == 1):                                        #1번 랜덤한 숫자를 뽑기 위한 random 함수를 사용하여 만듬
          s = random.randint(0,100)
          print(str(s)+"가(이) 추가되었습니다.")
          bst.insert(s)
        if(menu == 2):                                        #find함수를 사용하여 지우고싶은 숫자가 있는지 확인 후 있으면 삭제 없을 시엔 숫자가 없다고 표시함
          s = int(input("지우고 싶은 숫자를 알려주세요 : "))
          if(bst.find(s)==1):
            print(str(s)+"을(를) 성공적으로 지웠습니다.")
            bst.delete(s)
          else:
            print("지우고 싶은 숫자가 없습니다.")
        if(menu==3):                                          #find함수를 사용하여 지금 찾고있는 숫자가 있는지 확인함
          s = int(input("찾는 숫자를 알려주세요 : "))
          if(bst.find(s)==1):
            print(str(s) + "는 있습니다.")
          else:
            print("없습니다.")
        if(menu == 4):
          print("전체 숫자")
          for c in range(101):                                #0부터 101숫자까지 저장 되어있는 숫자들을 확인하기 위한 for문
            if(bst.find(c)==1):
              con +=1                                         #숫자를 뽑을때 마다 con변수에 +1씩 더함
              print(c, end = " ")
              if(con==10):                                    #뽑은 숫자가 10개일때 줄바꿈 후 con을 10으로 만듬
                print("")
                con =0
              if(c%3==0):                                     #뽑은 숫자중 3의 배수를 확인 후 count변수에 +1씩 더함
                count += 1
            
          print("")
          print(count)    
          print("")
          if(count >= 10):                                    #3의 배수가 10개 이상이면 성공했습니다를 출력 아니면 실패입니다를 출력함
            print("성공햇습니다.")
            
          else:
            print("실패입니다.")
        if(menu == 5):                                        #레벨 순회 표시
          clear.clr()
          bst.level_order_traversal()
        if(menu == 6):
          break
      else:
        clear.clr()                                           #1~5의 숫자가 아닌 다른 숫자를 넣엇을때 다시 적어달라는 표시를 함
        print("다시 적어주세요")
  elif(game == 2):                                            #게임 종료
    break
  else:                                                       #1~2의 숫자가 아닌 다른 숫자를 넣엇을때 다시 적어달라는 표시를 함
    print("1번과 2번중에 골라주세요.")
  
