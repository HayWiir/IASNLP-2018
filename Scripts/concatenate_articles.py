#python3
"""
created by kunal on 04-07-2018@17:11

Concatenates all the text files into one single text file
"""
all_files = [str(i) for i in range(1,301)] 
all_files = set(all_files)
skip_files = {'84', '140', '42'}

good_files = all_files - skip_files
good_files = list(good_files)
good_files.sort()

filenames = []
for indexval in good_files:
    #parses xml file
    str_index=str(indexval)
    tagged_file ='C-' + str_index + '.txt'
    filenames.append(tagged_file)
print(filenames)

with open('final.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)