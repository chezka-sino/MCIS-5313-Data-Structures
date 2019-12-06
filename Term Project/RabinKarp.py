from Bio import SeqIO
# from urllib.request import urlopen
import time

def search(pattern, string):

    return False

if __name__ == "__main__":
    # "https://hpc.csiro.au/users/317836/KELLY/BASE_Albany/reveg_16S/picrust/97_otus.fasta"

    fileName = "97_otus.fasta"
    pattern = "GGTAACGGCCCACCAAGGCGACGACGGGTAGCTGGTCTGAGAGGATGGCCAGCCACATTGGGACTG"

    inputFile = open(fileName, "r")
    fasta_iterator = SeqIO.parse(inputFile, "fasta")
    line_counter = 0

    # Start timer
    search_time = 0

    for fasta in fasta_iterator:
        name, sequence = fasta.id, str(fasta.seq)
        line_counter += 2

        # Start timer for current sequence
        # Start time here to exclude read time for fasta file
        start = time.time()

        search(pattern,sequence)

        end = time.time()

        # Add time to previous search time
        search_time+=end-start