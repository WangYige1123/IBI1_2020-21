genetic_code = {
        'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S',
        'TCG':'S','TAT':'Y','TAC':'Y','TAA':'O','TAG':'U','TGT':'C','TGC':'C',
        'TGA':'X','TGG':'W','CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P',
        'CCC':'P','CCA':'P','CCG':'P','CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
        'CGT':'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'J',
        'ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'B',
        'AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GTT':'V',
        'GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
        'GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G',
        'GGG':'G'}        
seq = 'ATGCGACTACGATCGAGGGCC'
def translation(seq):
    amino_acid_sequence = " "
    for start in range(0,len(seq) - 2, 3):
        stop = start + 3
        codon = seq[start:stop]
        aa = genetic_code.get(codon.upper(),'X')
        amino_acid_sequence = amino_acid_sequence + aa
    return(amino_acid_sequence)

print(translation(seq))


