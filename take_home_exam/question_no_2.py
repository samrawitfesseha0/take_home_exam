'''
Created on may 20, 2023

@author: Samrawit Fesseha
'''
# finding the total number of let_7 family of miRNA in the given mature.fa database

import sys
import os

def total_no_of_let7_miRNA(filename):
    if not os.path.isfile(filename):
        print("The specified file does not exist.")
        return

    species_codes = []
    species_frequency = {}

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('>'):
                miRNA_identifier = line[1:].strip()
                if 'let-7' in miRNA_identifier:
                    species_code = miRNA_identifier.split("-")[0]
                    species_codes.append(species_code)
                    species_frequency[species_code] = species_frequency.get(species_code, 0) + 1
    total_let7miRNA = len(species_codes)
    total_species = len(species_frequency)

    print("Total number of let-7 family of miRNAs:", total_let7miRNA)

    if total_species > 0:
        print("Total number of species codes with let-7 miRNA:", total_species)
    else:
        print("There are no species codes with let-7 miRNA in the file.")


def main(argv=None):
    if argv is None:
        argv = sys.argv
        
    filename = r"C:\Users\user\AP\exam\mature.fa"
    total_no_of_let7_miRNA(filename)
               
        
if __name__ == '__main__':

    sys.exit(main())        

