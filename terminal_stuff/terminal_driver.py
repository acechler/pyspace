import sys
from termcolor import colored
from datastructures import Graph, Node


class DecisionTest:
    def __init__(self):
      pass
    def run(self):
       values = [1,2,3,4,5,6,7,8,9,10]
       for i in values:
              if i % 2 == 0:
                print("Not Weird")
              else:
                print("Weird")
 

class TerminalDriver:
    def __init__(self):
        pass
        

    @staticmethod
    def run():
       print(colored("Hello World",'green'),end=" ")
