#!/usr/bin/env python

nucleotides = {'A':0, 'T':0, 'C':0, 'G':0, 'other':0}

input_filename = 'CDKN2A.fasta'
input_file = open(input_filename, 'rt')

for input_string in input_file:
    input_string = input_string.strip()
    if not input_string.startswith('>'):
        for n in input_string:
            n = n.upper()
            if n in nucleotides.keys():
                nucleotides[n] += 1
            else:
                nucleotides['other'] += 1

print(nucleotides)
gc_content = (nucleotides['G'] + nucleotides['C']) / (nucleotides['A'] + nucleotides['T'] + nucleotides['G'] + nucleotides['C'])
print('GC Content: %0.2f' % gc_content)