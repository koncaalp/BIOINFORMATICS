
from itertools import combinations

from numpy import Inf
from sympy import substitution

seq1 = "TATGCCAGTAGTCA"
seq2 = "ATGACTGTTCA"

subMatrix = {
    "A": {"A": 2, "C": -7, "G": -5, "T": -7, "-": -8},
    "C": {"A": -7, "C": 2, "G": -5, "T": -7, "-": -8},
    "G": {"A": -5, "C": -5, "G": 2, "T": -7, "-": -8},
    "T": {"A": -7, "C": -7, "G": -7, "T": 2, "-": -8},
    "-": {"A": -8, "C": -8, "G": -8, "T": -8, "-": 0},
}

def scorePair(seq1, seq2, subMatrix,gapOpen=-8,gapExtension=-6):
    assert len(seq1) == len(seq2), "Sequences should be equal in length"  
    score = 0
    for i in range(0,len(seq1)):
        nucleotide1 = seq1[i]
        nucleotide2 = seq2[i]
        score += subMatrix[nucleotide1][nucleotide2]
        if ((nucleotide1 == "-" and seq1[i-1] == "-") or (nucleotide2 == "-" and seq2[i-1] == "-")):
            score+= 2
    return score

def alignPair(seq1,seq2):
    numberOfGaps = len(seq1) - len(seq2)
    alignmentLength = max(len(seq1),len(seq2))
    positions = list(range(0,alignmentLength))

    gapPositionSets = list(combinations(positions, numberOfGaps))


    allSeq2 = []
    for gapPositions in gapPositionSets:
        pos = 0
        bestAlignedSeq2 = ''
        for i in range(0,alignmentLength):
            if i in gapPositions:
                bestAlignedSeq2 += '-'
            else:
                bestAlignedSeq2 += seq2[pos]
                pos += 1
        allSeq2.append(bestAlignedSeq2)



    bestScore = -Inf
    bestAlignments = []
    for bestAlignedSeq2 in allSeq2:
        

        currentScore = scorePair(seq1 ,bestAlignedSeq2, subMatrix)
        if currentScore == bestScore:
            bestAlignments.append(bestAlignedSeq2)
        elif currentScore > bestScore:
            bestAlignments = []
            bestAlignments.append(bestAlignedSeq2)
            bestScore = currentScore
    
    return seq1, bestAlignments, bestScore

seq1, bestAlig, score = alignPair(seq1, seq2)
print("Best Alignments:")
print(bestAlig)
print("Best Score:")
print(score)
