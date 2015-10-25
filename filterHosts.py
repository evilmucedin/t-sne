#!/usr/bin/env python3

fIn = open("2015-10-01-False-TopHosts2")
hosts = set()
iLine = 0
for line in fIn:
    if iLine < 5000:
        hosts.add( line.split("\t")[0] )
    else:
        break
    iLine += 1

fData = open("hosts.txt")
fOut = open("hosts.5000.txt", "w")
for line in fData:
    if line.split()[0] in hosts:
        print(line.strip(), file=fOut)
