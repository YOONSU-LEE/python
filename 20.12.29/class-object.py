#클래스: 함수+변수 모아놓은거(빵틀)
#오브젝트: 클래스 써서 만든거(빵)
#object == instance
#__init__ : self를 첫 인자로 받고 person에서 새로 쓸 변수들을 설정할 수 있다.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def say_hello(self, to_name): #self - 만들어진 물체의 변수를 활용 해야될 때
    print("안녕! " + to_name + " 나는 " + self.name)

  def introduce(self):
    print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

class Police(Person): #Police라는 클래스가 person를 상속하는 것이다.
  def arrest(self, to_arrest):
    print("넌 채포됐다, " + to_arrest)

class Programmer(Person):
  def program(self, to_program):
    print("다음엔 뭘 만들지? 아 이걸 만들어야겠다: " + to_program)

yoonsu = Person("윤수", 20)
jenny = Police("제니", 20)
michael = Programmer("마이클", 20)

jenny.introduce()
jenny.arrest("윤수")

michael.introduce()
michael.program("python")