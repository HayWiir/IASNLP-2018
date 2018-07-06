import os
import sys

file_dir = sys.argv[1]

filelist = os.listdir(file_dir)

for input_file in filelist:
    print input_file
    f = open(file_dir + input_file, 'r')
    lines = f.readlines()
    # print len(lines)
    # print lines[2]
    # print '%%%%%%%%%%%%%%%'
    # print lines[1]

    f = open('hindi.input.txt', 'w')
    f.write(lines[2])
    f = open('hindi.input.txt','r')
    lines = f.readlines()
    # print lines
    # print '%%%%%%%%%%%'
    # for line in lines:
    #     if linecount > 1:
    #         f.write(line)
    #     linecount += 1
    os.system('make')
    cmd = 'cp hindi.output outputs/' + input_file + '_output'
    print cmd
    os.system(cmd)
    # break
