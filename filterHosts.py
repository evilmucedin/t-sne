#!/usr/bin/env python3

import gzip

N = 1000

fIn = open("2015-10-01-False-TopHosts2")
hosts = []
for line in fIn:
    parts = line.strip().split("\t")
    hosts.append( (parts[0], int(parts[1])) )

hosts = sorted(hosts, key=lambda x: -x[1])

sHosts = set()
for i in range(N):
    sHosts.add(hosts[i][0])
    if i < 10:
        print(hosts[i][0])

fData = gzip.open("hosts.txt", "rt")
fOut = open("hosts.%d.txt" % N, "w")
for line in fData:
    if line.split()[0] in sHosts:
        print(line.strip(), file=fOut)
