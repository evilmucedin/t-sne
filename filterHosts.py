#!/usr/bin/env python3

fIn = open("2015-10-01-False-TopHosts2")
hosts = []
for line in fIn:
    parts = line.strip().split("\t")
    hosts.append( (parts[0], int(parts[1])) )

hosts = sorted(hosts, key=lambda x: -x[1])

sHosts = set()
for i in range(5000):
    sHosts.add(hosts[i][0])
    if i < 10:
        print(hosts[i][0])

fData = open("hosts.txt")
fOut = open("hosts.5000.txt", "w")
for line in fData:
    if line.split()[0] in sHosts:
        print(line.strip(), file=fOut)
