
def fastafilereader(filename):
    """
    Reads a fasta file and returns a dictionary with the name of the sequence as key and the sequence as value.
    """
    fasta_dict = {}
    with open(filename) as fasta_file:
        for line in fasta_file:
            if line.startswith('>'):
                name = line.strip()[1:]
                fasta_dict[name] = ''
            else:
                fasta_dict[name] += line.strip()
    return fasta_dict


print(fastafilereader('seq.fa'))