import sys
from termcolor import colored

class DecisionTest:
    def __init__(self):
      pass
    def run(self):
      n = int(input().strip())
      if n % 2 == 0:
        if 2 <= n <= 5:
           print("Not Weird")
        if 6 <= n <= 20:
           print("Weird")
        if n > 20:
           print("Not Weird")
      else:
        print("Weird")
 
class NoString:
   def __init__(self):
      pass
   def run(self):
      n = int(input())
      for i in range(1,n+1,1):
         print(i, end="")

class TerminalDriver:
    def __init__(self):
        pass
        

    @staticmethod
    def run():
      ns = NoString()
      ns.run()
       #dtest = DecisionTest()
       #dtest.run()
       #print(colored("Hello World",'green'),end=" ")
       