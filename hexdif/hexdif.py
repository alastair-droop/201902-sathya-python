#!/usr/bin/env python
# This script finds the most "different" k-mer from a given set of k-mers
# Alastair Droop, 2019-02-06

####################################################################################################
# The challenge is as follows:
# There are 4096 (4^6) possible DNA hexamers
# (for example AAAAAA, AAAAAT, AAAAAC, AAAAAG, AAAATA, ...)
#
# Given a list of 400 hexamers, find a new hexamer that is the most possible 
# 'different' hexamer from that list of hexamers.
#
# Suppose that we are concerned with DNA duplex hexamers, find also the most possible 
# 'different' duplex hexamer?
#     duplex ex.- AAAAAA     TTTTTT
#                 ||||||  =  ||||||
#                 TTTTTT     AAAAAA
#
#
# ANALYSIS:
# Can your code work for longer k-mers? At what k-mer length does your code become a 
# processing nightmare?
#
#
# DISCUSSION ON EXTENSION FEASIBILITY/STRATEGY:
# Suppose we wanted to find the most possible 'different' 20-mer in an entire genome 
# (so the list is now all 20-mers in a whole genome!) - perhaps that's not even realistically 
# possible...
# What (if any) are some strategies that you might employ in order to find the most 
# possible 'different' (or at least a very 'different') 20-mer?
####################################################################################################

# We are defining "most different from a set of kmers" as a kmer that has
# the lowest number of bases at a given position shared with the input kmers.
# NB: I don't understand what they are asking about the duplex hexamers; so I've not answered that.

# Get the necessary imports:
from sys import exit, stderr

# Define a function that exists with an error:
def error(message, code=1):
    print('ERROR: %s' % message, file=stderr)
    exit(code)

# Define the set of valid nucleotides:
alphabet = ('A', 'C', 'G', 'T')
print('using %d-letter alphabet "%s"' % (len(alphabet), ''.join(alphabet)))

# Define the k-mer length:
# NB: If None, define as length of first entry in file
k = None

# Load the input k-mers from file:
# NB: Load into a set to prevent duplicates; then get the number of
# unique kmers before converting back to a list.
input_filename = 'hexamers.txt'
print('reading k-mers from "%s"...' % input_filename)
input_kmers = set()
try:
    with open(input_filename, 'rt') as input_file:
        for line in input_file:
            line = line.strip()
            for base in line:
                if base not in alphabet: error('Invalid letter "%s" in kmer "%s"' % (base, line))
                if k is None: k = len(line)
                if len(line) != k: error('kmer "%s" is not of length %d' % (line, k))
            input_kmers.add(line[0:(k+1)])
except: error('failed to process input file "%s"' % input_filename)
n_kmers = len(input_kmers)
input_kmers = list(input_kmers)
print('%d unique %d-mers read from file' % (n_kmers, k))

# Determine the maximum number of k-mers we could have generated:
max_kmers = len(alphabet) ** k
print('%d possible %d-mers with %d-letter alphabet' % (max_kmers, k, len(alphabet)))
if n_kmers == max_kmers: error('all possible %d-mers in input data' % k)

# Build a consensus for each position in the k-mers. Sort the consensus so that
# the least frequent letters are first:
input_consensus = []
for i in range(0, k):
    bases = [input_kmers[j][i] for j in range(0, n_kmers)]
    pos_consensus = [(b, bases.count(b)) for b in alphabet]
    pos_consensus.sort(key=lambda x: x[1], reverse=False)
    input_consensus.append(pos_consensus)

# Print the consensus (if print_consensus is True):
print_consensus = True
if print_consensus is True:
    for i in range(0, k):
        print('sorted consensus at position %d:' % (i + 1))
        for j in input_consensus[i]:
            print(' %s: %d' % (j[0], j[1]))
    
# We can now build a new k-mer using the least frequent letter for each
# position. We know there is at least one to find (as we checked above).
output_kmer = ''.join([input_consensus[i][0][0] for i in range(0, k)])

# Check that output_kmer is not in the input list
# (I don't think it can be...):
if output_kmer in input_kmers: error('selected existing kmer')

# Otherwise, we're done:
print('most different %d-mer from input set is %s' % (k, output_kmer))
