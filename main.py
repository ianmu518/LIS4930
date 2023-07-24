file = open('sample_DNA.txt', 'r') #text file with a sequence of 'G', 'C', 'T', and 'A' characters
data = file.read()

print("DNA sequence:")
print(data)
print()

table01 = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'} #Changes of nucleotides during transcription

table02 = {
    "UUU": "Phenylalanine-", "UUC": "Phenylalanine-", "UUA": "Leucine-", "UUG": "Leucine-",
    "UCU": "Serine-", "UCC": "Serine-", "UCA": "Serine-", "UCG": "Serine-",
    "UAU": "Tyrosine-", "UAC": "Tyrosine-", "UAA": "STOP CODON", "UAG": "STOP CODON",
    "UGU": "Cysteine-", "UGC": "Cysteine-", "UGA": "STOP CODON", "UGG": "Tryptophan-",
    "CUU": "Leucine-", "CUC": "Leucine-", "CUA": "Leucine-", "CUG": "Leucine-",
    "CCU": "Proline-", "CCC": "Proline-", "CCA": "Proline-", "CCG": "Proline-",
    "CAU": "Histidine-", "CAC": "Histidine-", "CAA": "Glutamine-", "CAG": "Glutamine-",
    "CGU": "Arginine-", "CGC": "Arginine-", "CGA": "Arginine-", "CGG": "Arginine-",
    "AUU": "Isoleucine-", "AUC": "Isoleucine-", "AUA": "Isoleucine-", "AUG": "Methionine-",
    "ACU": "Threonine-", "ACC": "Threonine-", "ACA": "Threonine-", "ACG": "Threonine-",
    "AAU": "Asparagine-", "AAC": "Asparagine-", "AAA": "Lysine-", "AAG": "Lysine-",
    "AGU": "Serine-", "AGC": "Serine-", "AGA": "Arginine-", "AGG": "Arginine-",
    "GUU": "Valine-", "GUC": "Valine-", "GUA": "Valine-", "GUG": "Valine-",
    "GCU": "Alanine-", "GCC": "Alanine-", "GCA": "Alanine-", "GCG": "Alanine-",
    "GAU": "Aspartic Acid-", "GAC": "Aspartic Acid-", "GAA": "Glutamic Acid-", "GAG": "Glutamic Acid-",
    "GGU": "Glycine-", "GGC": "Glycine-", "GGA": "Glycine-", "GGG": "Glycine-"
} #Translation of all 64 possible codons into their amino acid or "STOP CODON"


def transcription(): #replaces each character in data according to table01 and prints result
    rna_sequence = ""

    for i in range(0, len(data)): 
        if data[i] in table01.keys():
            rna_sequence += table01[data[i]]
    print("RNA sequence:")
    print(rna_sequence)
    print()


transcription()


def translation(): #replaces each character in data according to table01 then translates the result into a sequence of amino acids according to table02
    rna_sequence = ""
    amino_acid_sequence = ""

    for i in range(0, len(data)):
        if data[i] in table01.keys():
            rna_sequence += table01[data[i]]

    if len(rna_sequence) % 3 == 0: #If rna_sequence has a number of characters that are a multiple of three
        for i in range(0, len(rna_sequence), 3):
            codon = rna_sequence[i:i + 3]
            amino_acid_sequence += table02[codon]
        print("Translated Amino Acid polypeptide chain:")
        print(amino_acid_sequence)
    else:
        print("RNA Sequence could not be translated into amino acids")
        print("as the number of nucleotides in the sequence are not")
        print("a multiple of three.")


translation()
