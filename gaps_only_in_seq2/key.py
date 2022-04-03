from math import inf
from itertools import combinations


seq1 = "TATGCCAGTAGTCA"
seq2 = "ATGACTGTTCA"

GP = -8

subMatrix = {
    "A": {"A": 2, "T":-7, "G":-5, "C":-7, "-": GP},
    "T": {"A": -7, "T":2, "G":-7, "C":-5, "-": GP},
    "G": {"A": -5, "T":-7, "G":2, "C":-7, "-": GP},
    "C": {"A": -7, "T":-7, "G":-5, "C":2, "-": GP},
    "-": {"A": GP, "T":GP, "G":GP, "C":GP, "-":0}
}

def scorePair(seq1, aligned_seq2, subMatrix,gapOpen=-8,gapExtension=-6):
    score = 0
    assert len(seq1) == len(aligned_seq2), "Lengths must be equal"
    for i in range(len(seq1)):          #check if gap is opening or extension
        if aligned_seq2[i] == '-':
            if i != 0 and aligned_seq2[i-1] == '-':
                score += gapExtension
            else:
                score += gapOpen
        else:               #if it is not gap add score from matrix
            score += subMatrix[seq1[i]][aligned_seq2[i]]
    return score


def alignPair(seq1,seq2):
    numberOfGaps = abs(len(seq1) - len(seq2))
    alignment_length= max(len(seq1), len(seq2))
    positions= []
    for i in range (0,alignment_length): #get all positions possible
        positions.append(i)

    gapPositionsSets = combinations(positions, numberOfGaps) #get combination of positions for gaps to be in

    bestAlignedSeq2 = ''
    best_score = -inf
    

    
    aligned_sequences=[]
    for gapPositions in gapPositionsSets: #for every combination of positions
        pos=0
        aligned_sequence=""
        for i in range (0,alignment_length): 
            if i in gapPositions: #if it needs to be gap put gap
                aligned_sequence += "-"
            else: 
                aligned_sequence += seq2[pos] #else put the corresponding letter from seq2 and increase the last position put
                pos+=1
        aligned_sequences.append(aligned_sequence)
    

    best_alignments= []
    for aligned_seq in aligned_sequences: #score every alignment and get the best one 
        current_score= scorePair(seq1, aligned_seq,subMatrix)
        if current_score > best_score:
            best_alignments = [] #delete previous alignments
            best_score = current_score
            best_alignments.append(aligned_seq)
        elif current_score == best_score:
            best_alignments.append(aligned_seq)

    return seq1, best_alignments, best_score



seq1, bestseq2, score = alignPair(seq1,seq2)
print(bestseq2)
print(score)