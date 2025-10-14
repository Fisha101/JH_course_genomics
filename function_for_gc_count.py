#function to compute gc percentage of a dna sequence

def gc(dna):
    "what it does: a function to compute gc percentage of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

help(gc)

