'''
Created on Jun 1, 2023

@author: Samrawit Fesseha
'''
import sys
import matplotlib.pyplot as plt
import numpy as np
import os

class MiRNAAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.let7_species = {}

    def extract_let7_code(self, header):
        if 'let-7' in header:
            code = header.split('let-7')[1].split()[0]
            return f"let-7{code[0]}"
        return ""

    def extract_species_code(self, header):
        start_index = header.find('>') + 1
        end_index = header.find('-', start_index)
        if start_index < end_index:
            return header[start_index:end_index]
        return ""

    def process_file(self):
        if not os.path.isfile(self.filename):
            print("The specified file does not exist.")
            return

        current_species = ""

        with open(self.filename, 'r') as file:
            for line in file:
                if line.startswith('>'):
                    header = line[1:].strip()
                    current_species = self.extract_species_code(header)
                else:
                    let7_code = self.extract_let7_code(header)
                    if let7_code:
                        self.let7_species.setdefault(current_species, {}).setdefault(let7_code, 0)
                        self.let7_species[current_species][let7_code] += 1

    def plot_let7_family_presence(self):
        let7_species_filtered = {species: counts for species, counts in self.let7_species.items() if sum(counts.values()) >= 5}

        species_list = list(let7_species_filtered.keys())
        let7_codes = list(set().union(*[d.keys() for d in let7_species_filtered.values()]))

        presence_matrix = np.zeros((len(species_list), len(let7_codes)))

        for i, species in enumerate(species_list):
            for j, let7_code in enumerate(let7_codes):
                presence_matrix[i, j] = let7_species_filtered[species].get(let7_code, 0)

        x = np.arange(len(species_list))
        bar_width = 0.35

        fig, ax = plt.subplots(figsize=(10, 6))

        bottom = np.zeros(len(species_list))

        for i, let7_code in enumerate(let7_codes):
            ax.bar(x, presence_matrix[:, i], bottom=bottom, label=let7_code)
            bottom += presence_matrix[:, i]

        ax.set_xlabel('Species')
        ax.set_ylabel('Presence Count')
        ax.set_title('Presence of let-7 Family per Species')
        ax.set_xticks(x)
        ax.set_xticklabels(species_list, rotation=45, ha='right')
        ax.legend()

        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        self.process_file()
        self.plot_let7_family_presence()



def main(argv=None):
    if argv is None:
        argv = sys.argv
    
filename = r"C:\Users\user\AP\exam\mature.fa"
analyzer = MiRNAAnalyzer(filename)
analyzer.run_analysis()                  
  
if __name__ == '__main__':

    sys.exit(main())        