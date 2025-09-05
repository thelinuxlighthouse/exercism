def to_rna(dna_strand):
    dnaTOrna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([dnaTOrna[chr] for chr in dna_strand])