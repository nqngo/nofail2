# API-compatible input() function
def input():
    import sys

    return  "".join(line for line in sys.stdin)

STDIN=input()

# Solution
PARSED=STDIN.split()

# Input parsing
S=PARSED[0]
N=int(PARSED[1])
WORDLIST=PARSED[2:(2+N)]

# Constraint checking
if len(S) > 300:
    print("False")
    exit(1)
if N > 1000:
    print("False")
    exit(1)


def splits(text, L=20):
    "Return a list of all possible (first, rem) pairs, len(first)<=L."
    return [(text[:i+1], text[i+1:]) 
            for i in range(min(len(text), L))]


def segment(text):
    """ Recursively segment the word and check if the first word is in wordlist. """
    if not text: return []
    candidates = [ [first] + segment(rem) for first, rem in splits(text)
                    if first in WORDLIST 
                 ]
    return candidates


def flatten_deep(arr: list):
    """ Flattens arbitrarily-nested list `arr` into single-dimensional. """

    while arr:
        if isinstance(arr[0], list):  # Checks whether first element is a list
            arr = arr[0] + arr[1:]  # If so, flattens that first element one level
        else:
            yield arr.pop(0)  # Otherwise yield as part of the flat array


# Check the candidate if it can reconstitute into the input word
# then print True otherwise False
for candidate in segment(S):
    flat_candidate = list(flatten_deep(candidate))
    if "".join(flat_candidate) == S:
        print("True", end = '')
        exit(0)
print("False", end = '')
exit(0)