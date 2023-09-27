import time, os
import bext

print("Rainbow Time!")
print("Press Ctrl-C to stop.")

time.sleep(3)

indent = 0
indentIncreasing = True

while True:
    print(" " * indent, end="")

    bext.fg("red")
    print("##", end="")

    bext.fg("yellow")
    print("##", end="")

    bext.fg("green")
    print("##", end="")

    bext.fg("blue")
    print("##", end="")

    bext.fg("cyan")
    print("##", end="")

    bext.fg("purple")
    print("##")

    if indentIncreasing:
        indent += 1
    else:
        indent-=1
    
    
    if indent == os.get_terminal_size()[0] - 12:
        indentIncreasing = False
    if indent == 0:
        indentIncreasing = True
    time.sleep(0.03)
