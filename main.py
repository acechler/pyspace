import sys

from pygame_stuff.pygame_driver import PygameDriver
from terminal_stuff.terminal_driver import TerminalDriver

def main():
    # Initialize and run the pygame instance
     #driver = PygameDriver()
     driver = TerminalDriver()
     driver.run()


if __name__ == "__main__":
    main()