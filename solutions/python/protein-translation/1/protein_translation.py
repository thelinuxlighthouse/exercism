def proteins(strand):
    codon_protein = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}

    codons_list = []
    protein = []

    for i in range(0, len(strand), 3):
        codons_list.append(strand[i:i+3])

    for codon in codons_list:
        if codon_protein[codon] == 'STOP':
            break
        else:
            protein.append(codon_protein[codon])
    return protein
