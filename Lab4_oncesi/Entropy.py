from math import log
seq = "ATGC"
def entropy(positionString):
    uniqLetters = list(set(positionString))
    H = 0
    for letter in uniqLetters:
        P = positionString.count(letter) / len(positionString)
        H += P * log(1/P, 2)

    return H

print(entropy(seq))