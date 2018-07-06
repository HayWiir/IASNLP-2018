import os


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

files = os.listdir('.')

files = [f for f in files if 'output' not in f and 'py' not in f]
# print files
files.sort(key=lambda f: int(filter(str.isdigit, f)))
files = files[:50]


for file in files:
    print file, file_len(file)
