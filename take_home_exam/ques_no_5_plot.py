'''
Created on Jun 15, 2023

@author: user
'''
import sys
import os
import Levenshtein
import matplotlib.pyplot as plt

class LevenshteinDistanceAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.let7_sequences = {}
        self.let7_frequency = {}
        self.avg_distances = []
        self.frequencies = []
        self.miRNA_families = []

    def average_levenshtein_distance(self):
        if not os.path.isfile(self.filename):
            print("The specified file does not exist.")
            return

        with open(self.filename, 'r') as file:
            let7_code = ""
            sequence = ""
            for line in file:
                if line.startswith('>'):
                    header = line[1:].strip()
                    let7_code = self.extract_let7_code(header)
                    sequence = ""
                else:
                    sequence = line.strip()

                if let7_code and sequence:
                    self.let7_sequences.setdefault(let7_code, []).append(sequence)
                    self.let7_frequency[let7_code] = self.let7_frequency.get(let7_code, 0) + 1

        total_sequences_count = 0

        for let7_code, sequences in self.let7_sequences.items():
            total_distance = 0
            total_pairs = 0

            if len(sequences) < 2:
                continue

            for i in range(len(sequences) - 1):
                for j in range(i + 1, len(sequences)):
                    total_distance += Levenshtein.distance(sequences[i], sequences[j])
                    total_pairs += 1

            average_distance = total_distance / total_pairs
            frequency = self.let7_frequency.get(let7_code, 0)
            self.avg_distances.append(average_distance)
            self.frequencies.append(frequency)
            self.miRNA_families.append(let7_code)
            print(f"The Average Levenshtein distance among all pairs for miRNA family {let7_code}: {average_distance:.2f}")
            print(f"The frequency of miRNA family {let7_code}: {frequency}")
            total_sequences_count += frequency

        print(f"Total sequences count: {total_sequences_count}")

        self.plot_results()

    def extract_let7_code(self, header):
        if 'let-7' in header:
            code = header.split('let-7')[1].strip()[0]
            return f"let-7{code}"
        return ""

    def plot_results(self):
        x_pos = range(len(self.miRNA_families))
        fig, ax1 = plt.subplots()
        ax1.bar(x_pos, self.avg_distances, align='center', alpha=0.5)
        ax1.set_ylabel('Average Levenshtein Distance')
        ax1.set_title('Average Levenshtein Distance and Frequency for miRNA Families')

        ax2 = ax1.twinx()
        ax2.plot(x_pos, self.frequencies, 'r')
        ax2.set_ylabel('Frequency')

        plt.xticks(x_pos, self.miRNA_families)
        plt.xlabel('miRNA Family')

        plt.show()


def main(argv=None):
    if argv is None:
        argv = sys.argv
        
filename = r"C:\Users\user\AP\exam\mature.fa"
analyzer = LevenshteinDistanceAnalyzer(filename)
analyzer.average_levenshtein_distance()
        
               
  
if __name__ == '__main__':

    sys.exit(main())  