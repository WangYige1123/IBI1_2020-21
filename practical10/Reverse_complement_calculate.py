def g(sequence):
    translate = {'C':'G','G':'C','A':'T','T':'A'}
    new_sequence = ''
    for n in range(0,len(sequence),1):
        new_sequence = translate[sequence[n]] + new_sequence
    print (new_sequence)
sequence = 'GCATCTG'
g(sequence)
