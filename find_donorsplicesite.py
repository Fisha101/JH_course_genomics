

#given a DNA sequence find postions of all donor splice site candidates

dna = input("Enter your DNA sequence, please:")
position = dna.find('gt',0) #position of donor splice site
found = False

while position>-1:
    print("Donor splice site candidate at position %d"%position)
    position=dna.find('gt',position+1)
    
if not found:
    print("No donor splice site candidates found.")
