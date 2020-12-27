# for while
# while문은 조건을 달 수 있다.
i = 0

while True:
  print(i)
  print("안녕")
  print("hi")
  i = i + 1

  if i > 2:
    break


for i in range(100):
  print(i)
  print("안녕")
  print("hi")
  i = i + 1

  if i > 10:
    break


i = 0

for i in range(3):
  print(i)
  print("안녕")
  print("hi")

  if i==1:

    continue #특이한 조건에서 밑에 코드를 실행시키고 싶지 않을 때 
  
  print("뭐해")



#리스트 x = list[] or []  딕셔너리
#인덱스 안에 몇가지 있는지 
x = [1,2,3,4]

num_elements = len(x)
print(num_elements)

#인덱스 순서대로 나열하기
x = [4,2,3,1]

y = sorted(x)
print(y)

#인덱스 안의 값들 합치기

x = [4,2,3,1]

z = sum(x)
print(z)


x = [4,2,3,1]

for n in x:
  print(n)


  #엘레먼트 찾기

x = [4,2,3,1]
y = ["hello", "there"]

print(x.index(3))
print(y.index("hello"))


x = [4,2,3,1]
y = ["hello", "there"]

print("hello" in y)



x = [4,2,3,1]
y = ["hello", "there"]

if "hello" in y:
  print("hello 가 있어요")


#튜플 x = tuple() or ()
#tuple에서는 assignment가 안된다.
# *assignment = 튜플 안의 값을 업데이트 하는 것

#mutable(가변): 값을 바꿀 수 있음
#immutable(불변): 값을 바꿀 수 없음

#list는 가변, tuple은 불변



#딕셔너리-key 랑 value로 이루어져 있는 자료구조

x = dict()
y = {}


#dictionary
x = {
  0 : "Yoonsu",
  1 : "Hello",
  "age" : 20,
}

print(x. keys())
print(x.values())

#엘리먼트 반복해서 돌아보기
for key in x:
  print("key:" + str(key))
  print("value:" + str(x[key]))

#dictionary도 key, value 둘다 assignment 가능


#예제
fruit = ["사과","사과","바나나","바나나","딸기","딸기","키위","복숭아","복숭아","복숭아",]
d = {}


for f in fruit:
  if f in d:
    d[f] = d[f] + 1
  else:
      d[f] = 1

print(d)

