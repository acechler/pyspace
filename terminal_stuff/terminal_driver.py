import sys
from termcolor import colored

class TerminalDriver:
    def __init__(self):
        pass

    @staticmethod
    def run():
       
       values = [1,2,3,4,5,6,7,8,9,10]
       for i in values:
              if i % 2 == 0:
                print(colored(i, 'green'), end=" ")
              else:
                print(colored(i, 'red'), end=" ")
