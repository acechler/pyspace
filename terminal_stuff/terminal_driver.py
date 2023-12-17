import sys
from termcolor import colored

class TerminalDriver:
    def __init__(self):
        pass

    @staticmethod
    def run():
       print(colored('Hello, world!', 'green', 'on_black', ['underline']))
       for i in range(1,10):
           # Print index i in green
              print(colored(i, 'green', 'on_black', ['underline']))
