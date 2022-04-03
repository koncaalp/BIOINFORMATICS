seq1 = "ATGCTATGCT"
seq2 = "GGCGGGCGTT"

alignmentList = []
alignment = []

def alignNextPosition(alignment, sub1, sub2):
    for state in ['match', 'gap1', 'gap2']: #for every pair try all cases
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

        alignedPair = (letter1, letter2) # get the tried case
        currentAlignment = list(alignment) 
        currentAlignment.append(alignedPair) #append the tried case

        if newSub1 == "" and newSub2 == "":         #use recursion, if both sequences are empty then append and finish
            alignmentList.append(currentAlignment)
        elif newSub1 == "":                         #if seq1 is empty then append gaps as many as leftovers in seq2
            for letter in newSub2:
                currentAlignment.append(('-', letter))
            alignmentList.append(currentAlignment)
        elif newSub2 == "":                         #same but vice versa
            for letter in newSub1:
                currentAlignment.append((letter, '-'))
            alignmentList.append(currentAlignment)
        else:                                       #if neither is empty call the function again
            alignNextPosition(currentAlignment,newSub1,newSub2)
        
alignNextPosition(alignment, seq1, seq2)   #call the function for the first time 

print(len(alignmentList))


for aln in alignmentList: #create the alignments
    alnSeq1 = ''
    alnSeq2 = ''
    for pair in aln:
        alnSeq1 += pair[0]
        alnSeq2 += pair[1]
    #print(alnSeq1)
    #print(alnSeq2)
    #print("")
    #print(alnSeq1+alnSeq2) #to see if all are unique pyton3 filename.py | sort | uniq -c
print(len(alignmentList))