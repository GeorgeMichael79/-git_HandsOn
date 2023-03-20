#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
from collections import Counter

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f' looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("We have FOUND moti in your sequence")
    else:
        print("We have NOT FOUND modif in your sequence")
#we have to count the occurences of each nucleotide in the seq
counts=Counter(args.seq)
# count the total number of nucleotides in the given seq
totalNo_nucleotides=sum(counts.values())
# % of each nucleotide
percentages = {nucleotide: count / totalNo_nucleotides * 100 for nucleotide, count in counts.items()}
#results of the percentages
print("Nucleotide percentages:")
for nucleotide, percentage in percentages.items():
  print(f"{nucleotide}: {percentage:.2f}%")

