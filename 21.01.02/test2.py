a = int(input())

temp=0

while True:
  temp+=1
  if temp > a:
    break
  if temp%2 == 1:
    print(temp)