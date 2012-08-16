#!/usr/bin/env python
#
# cat SGSN_00000058.dat.txt | grep dataVolumeGPRSDown | sed "s/#dataVolumeGPRSDownlink//" | sed "s/ //g" | python -u stats.py
import sys


stats = {'<100': 0, '101-1000':0, '1001-10000':0, '10001-100000':0,'>100000':0,}

while True:
    line = sys.stdin.readline()
    if not line: break
    if line[-1] == '\n': line = line[:-1]
    
    if int(line) < 100: 
        stats['<100'] += 1 
    elif int(line) > 101 and int(line) < 1000: 
        stats['101-1000'] += 1 
    elif int(line) > 1001 and int(line) < 10000: 
        stats['1001-10000'] += 1 
    elif int(line) > 10001 and int(line) < 100000: 
        stats['10001-100000'] += 1 
    elif int(line) > 100000: 
        stats['>100000'] += 1 
        
print stats