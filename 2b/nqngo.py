# API-compatible input() function
def input():
    import sys

    return  "".join(line for line in sys.stdin)

STDIN=input()

print(STDIN)