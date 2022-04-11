# from sympy import sequence


def fastareader(inputFile):
    myDict = {}
    sequence = ''
    filein = open(inputFile, 'r')
    for line in filein:
        if line[0] == ">":
            if sequence:
                myDict[header] = sequence
            header = line[1:].strip()
            sequence = ''

        else:
            sequence += line.strip()
    myDict[header] = sequence
    return myDict

print(fastareader('seq.fa'))