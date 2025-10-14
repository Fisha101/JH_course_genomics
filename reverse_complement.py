#a function to reverse complement a DNA sequence.

seq = input("Enter DNA sequence: ")

def reverse_string(seq):
    "returns the reverse sequence."
    return seq[::-1]

def complement(seq):
    "returns the complementary sequence."
    basecomplement= {'a':'t', 't':'a', 'g':'c', 'c':'g', 'n':'n'}
    letters = list(seq)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

def reversecomplement (seq) :
    "Return the reverse complement of the dna string."
    seq = seq.lower()
    seq = reverse_string(seq)
    seq = complement(seq)
    return seq


print("Reverse complement:", reversecomplement(seq))

