import os
import sys
import getch

def calculator():
    expression = ''
    buffer = ''
    reader = getch._Getch()
    while True:
        input_char = reader()
        if 'reset' in buffer:
            os.system('clear')
            buffer = ''
            expression = ''
        if input_char in ['+', '-', '/', '*']:
            expression += buffer
            expression += input_char
            buffer = ''
        elif input_char == '=':
            break
        result = eval(expression)
        print(result)

if __name__ == "__main__":
    # buffer = 0
    while True:
        result = calculator()
        print(result)

    # input_read = str(sys.stdin.readline())
    #
    # sys.stdout.write("[script2.py:] " + input_read + " input read\n")
    # sys.stdout.flush()