from enum import IntEnum
from typing import List, Tuple

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

# utility function to convert a str into a gene
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    n = len(s)
    for i in range(0, n, 3):
        if (i + 2) >= n:    # don't run off end!
            return gene
        #  initialize codon out of three nucleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)  # add codon to gene
    return gene


my_gene: Gene = string_to_gene(gene_str)
print(my_gene)


## Linear Search
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
        return False

acg: Gene = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Gene = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


# Binary search
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:  # while there is still a search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
















































