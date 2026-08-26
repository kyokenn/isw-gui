#!/usr/bin/env python3
# Script to split original isw.conf into separate files


with open('isw.conf', 'r') as fin:
    fout = None
    for line in fin.readlines():
        if line.startswith('['):
            name = line.strip('\n').strip('[]')
            fout and fout.close()
            fout = open(f'{name}.conf', 'w')
            fout.write(line)
        elif fout:
            fout.write(line)
