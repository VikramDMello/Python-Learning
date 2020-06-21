#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

  def method3(self, someNum):
    print(someNum)


class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, someString):
    print("anotherClass method2 ")

  def method3(self, someNum):
    print(someNum)


def main():
  c = myClass()
  c.method1()
  c.method2("This is a string")
  c.method3(5)

  c2 = anotherClass()
  c2.method1()
  c2.method2("This is a string")
  
  

  
if __name__ == "__main__":
  main()
