from Bio import SeqIO
import time

def calc_hash(text, d, q):
    hash_text = 0

    for i in range(len(text)):
        hash_text = (d * hash_text + ord(text[i]))% q

    return hash_text

def search(pattern, string):

    d = 4
    q = 11
    m = len(pattern)
    n = len(string)
    h = pow(d, m-1) % q

    # calculate hash of pattern and first m characters of string
    p = calc_hash(pattern,d,q)
    s = calc_hash(string[0:m],d,q)

    for i in range(0,n-m):

        if p == s:

            for j in range(m):
                # not a match
                if string[i+j] != pattern[j]:
                    break

            j+=1
            if j==m:
                return i

        if i < n-m:
            s = (d*(s-ord(string[i])*h) + ord(string[i+m])) % q

    return -1

if __name__ == "__main__":

    fileName = "97_otus.fasta"
    pattern = "GGTAACGGCCCACCAAGGCGACGACGGGTAGCTGGTCTGAGAGGATGGCCAGCCACATTGGGACTG"

    inputFile = open(fileName, "r")
    fasta_iterator = SeqIO.parse(inputFile, "fasta")
    line_counter = 0
    record_counter = 0
    num_found = 0

    # Start timer
    search_time = 0

    print("Key Pattern looking for:", pattern, "\n")

    for fasta in fasta_iterator:
        name, sequence = fasta.id, str(fasta.seq)
        record_counter += 1
        line_counter += 2

        # Start timer for current sequence
        # Start time here to exclude read time for fasta file
        start = time.time()

        index_match = search(pattern,sequence)
        if index_match >= 0:
            num_found+=1
            print("key was found at", name, "(Line, column):", line_counter, ",", index_match)
            print("NAME:", name)
            print()

        end = time.time()

        # Add time to previous search time
        search_time+=end-start

    print("Total Number of read:", record_counter)
    print("Total execution time:", search_time)