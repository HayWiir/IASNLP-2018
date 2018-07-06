import os
import io

file_list = os.listdir('.')

for file in file_list:
    print(file)
    root_name = '_'.join(file.split('_')[:-1])
    print(root_name)
    with io.open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            comp = line.split()
            if len(comp) > 2:
                line_to_add = comp[0] + '\t' + comp[2] + '\n'
                with io.open(root_name, mode='a', encoding='utf-8') as output:
                    output.write(line_to_add)
