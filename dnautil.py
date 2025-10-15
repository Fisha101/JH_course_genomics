#!/usr/bin/python

"dnautil module contains some functions for dna sequence analysis"

def gc(dna):
    "what it does: a function to compute gc percentage of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

dna = input("Enter DNA sequence: ")
frame_input = input("Enter reading frame (number) [press Enter to use default 0]: ")
if frame_input == "":
    frame = 0
else:
    frame = int(frame_input)

def has_stop_codon(dna, frame=0):
    'This program that checks if a given DNA sequence contains an in-frame stop codon.'
    dna.lower()
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3]
        if codon in stop_codons:
            stop_codon_found = True
            break
    
    if True :
        print('Input sequence has an in frame stop codon.')
    else:
        print('Input sequence does NOT have an in frame stop codon.')        
        
has_stop_codon(dna, frame)

