seq1 = "ATGCT"
seq2 = "GGCG"

alignmentList = []
alignment = []

def alignNextPosition(alignment, sub1, sub2):
    for state in ['match', 'gap1', 'gap2']:
        if state == 'match':
            letter1 = sub1[0]
            letter2 = sub2[0]
            newSub1 = sub1[1:]
            newSub2 = sub2[1:]
        elif state == 'gap1':
            letter1 = "-"
            letter2 = sub2[0]
            newSub1 = sub1
            newSub2 = sub2[1:]
        elif state == 'gap2':
            letter1 = sub1[0]
            letter2 = "-"
            newSub1 = sub1[1:]
            newSub2 = sub2

        alignedPair = (letter1, letter2)
        currentAlignment = list(alignment)
        currentAlignment.append(alignedPair)

        if newSub1 == "" and newSub2 == "": 
            alignmentList.append(currentAlignment)
        elif newSub1 == "":
            for letter in newSub2:
                currentAlignment.append(('-', letter))
            alignmentList.append(currentAlignment)
        elif newSub2 == "":
            for letter in newSub1:
                currentAlignment.append((letter, '-'))
            alignmentList.append(currentAlignment)
        else:
            alignNextPosition(currentAlignment,newSub1,newSub2)
        
alignNextPosition(alignment, seq1, seq2)

print(len(alignmentList))


for aln in alignmentList:
    alnSeq1 = ''
    alnSeq2 = ''
    for pair in aln:
        alnSeq1 += pair[0]
        alnSeq2 += pair[1]
    print(alnSeq1)
    print(alnSeq2)
    print("")

