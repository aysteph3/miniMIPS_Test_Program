
with open ('minimips_synth.v','r') as f: #input file
    each_data = f.readlines()

count = 0
for line in each_data:
    data = line.rstrip()
    for word in data.split():
        if ('FLIP_FLOP_D' in word):
            print word
            count = count+1
            
print count
    
