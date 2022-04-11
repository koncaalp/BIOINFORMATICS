from itertools import combinations
from sympy import sequence


sequence = "ATGT-AT-G"

combs = combinations(range(len(sequence)), 2)

score = 0
gapScore = -1
matchScore = 1
mismatchScore = -1

for comb in list(combs):
    letter1 = sequence[comb[0]]
    letter2 = sequence[comb[1]]
    if letter1 == letter2:
        score += matchScore
    elif letter1 == '-' or letter2 == '-':
        score += gapScore
    elif letter1 == '-' and letter2 == '-':
        score += 0
    else:
        score += mismatchScore

print(score)