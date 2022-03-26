
from itertools import combinations

from numpy import Inf
from sympy import substitution
#subMatrix here

# def scorePair(seq1, seq2, subMatrix):
#     assert seq1 == seq2, "Sequences should be equal in length"
#     score = 0
#     for i in range(0,len(seq1)):
#         nucleotide1 = seq1[i]
#         nucleotide2 = seq2[i]
#         score += subMatrix[nucleotide1][nucleotide2]
#     return score


seq1 = "ATGCGCTGAC"
seq2 = "ATCGTGC"

numberOfGaps = len(seq1) - len(seq2)
alignmentLength = max(len(seq1),len(seq2))
positions = list(range(0,alignmentLength))

gapPositionSets = list(combinations(positions, numberOfGaps))
print(list(gapPositionSets))


allSeq2 = []
for gapPositions in gapPositionSets:
    pos = 0
    alignedSeq2 = ''
    for i in range(0,alignmentLength):
        if i in gapPositions:
            alignedSeq2 += '-'
        else:
            alignedSeq2 += seq2[pos]
            pos += 1
    allSeq2.append(alignedSeq2)


print(allSeq2)

bestScore = -Inf
bestAlignments = []
for alignedSeq2 in allSeq2:
    currentScore = scorePair(seq1, seq2, substitutionMatrix)
    if currentScore == bestScore:
        bestAlignments.append(alignedSeq2)
    elif currentScore > bestScore:
        bestAlignments = []
        bestAlignments.append(alignedSeq2)
        bestScore = currentScore
    print(bestAlignments)

#gap extension penalty ne