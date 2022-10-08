import os
import sys

def calculator():
    buffer = ''
    reader = _Getch()
    while True:
        input_char = reader().decode()
        print(input_char, end='')
        if input_char == '=':
            break
        buffer += input_char
    result = eval(buffer)

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


if __name__ == "__main__":
    calculator()
    #getch = _Getch()
    #print(getch())
    # buffer = 0
    #while True:
    #    result = calculator()
    #    print(result)

    # input_read = str(sys.stdin.readline())
    #
    # sys.stdout.write("[script2.py:] " + input_read + " input read\n")
    # sys.stdout.flush()