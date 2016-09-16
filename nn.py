#!/usr/bin/env python

import sys

dim = 1
for line in open(sys.argv[1]):
    parts = line.strip().split()
    if len(parts) > 1:
        dim = len(parts) - 1

print "dim = %d" % dim

words = []
for line in open(sys.argv[1]):
    parts = line.strip().split()
    words.append( (parts[0], map(float, parts[1:1 + dim])) )

for i in xrange(len(words)):
    best = 1e9
    bestIndex = -1
    for j in xrange(len(words)):
        if i != j:
            dist = 0
            for k in xrange(dim):
                dist += (words[i][1][k] - words[j][1][k])**2
            if dist < best:
                best = dist
                bestIndex = j
    print("%s\t%s" % (words[i][0], words[bestIndex][0]))
