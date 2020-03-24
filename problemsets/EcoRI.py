#!/usr/bin/env python3
import sys
import re 

dna = sys.argv[1].upper()
ecoRI = "GAATTC"
ecoRI_rev = "CTTAAG"

readout="EcoRI Start Position: {} (cuts at {}) End Position: {} (cuts at {})"
readout2="EcoRI Start Position: {} (cuts at {}) End Position: {} (cuts at {}) (REVERSE STRAND)"

if ecoRI in dna:
    for cut in re.finditer(ecoRI, dna):
        start = cut.start()+1
        cut1 = start + 1
        end = cut.end()
        cut2 = end -1
        out = readout.format(start,cut1,end,cut2)
    print(out)
elif ecoRI_rev in dna:
    for cut in re.finditer(ecoRI_rev, dna):
        start = cut.start()+1
        cut1 = start + 1
        end = cut.end()
        cut2 = end -1
        out = readout.format(start,cut1,end,cut2)
    print(out)
