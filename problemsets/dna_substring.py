#!/usr/bin/env python3
import sys

dna=sys.argv[1]
dna = dna.upper()
sub = dna[99:200]

sub_list=list(map(str,sub))

#count number of guanines in dna seq
g_count = sub.count('G')

#Make reverse complementary strand
comp_dict = {'A':'T','T':'A','G':'C','C':'G'}
comp_seq=[]
for x in sub_list:
    comp_seq.append(comp_dict.get(x))
rev_comp = "".join(comp_seq[::-1])

print(sub,'\n', g_count,'\n', rev_comp)


