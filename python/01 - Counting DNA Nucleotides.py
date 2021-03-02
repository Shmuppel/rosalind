def nucleotide_counter(dna_string):
    """
    Prints a count of each DNA nucleotide in a given DNA string.
    :param dna_string: string to count nucleotides from.
    """
    nucleotides = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for char in dna_string:
        nucleotides[char] += 1

    print("Count of nucleotides:")
    print(f"A: {nucleotides['A']}")
    print(f"T: {nucleotides['C']}")
    print(f"G: {nucleotides['G']}")
    print(f"C: {nucleotides['T']}")


if __name__ == '__main__':
    nucleotide_counter("ACGT")