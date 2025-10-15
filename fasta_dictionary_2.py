#builds dictionary with all sequences form fasta file
try:
    f = open('my_seq.fasta')
except IOError:
    print ('file not found')
    

seqs_dict = {}
for line in f:
    line = line.rstrip()

    if line[0]=='>':
        words = line.split()
        name = words[0][1:]
        seqs_dict [name] = ''

    else :
        seqs_dict [name] = seqs_dict [name] + line
        
f.close()       

for name, seqs_dict in seqs_dict.items():
    print(name, seqs_dict)
