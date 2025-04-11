from Digit import Digit
from statistics import mode

class DigitMatcher:
    def __init__(self, file_path):
        self.digits = []
        with open(file_path, 'r') as f:
            for line in f:
                values = line.strip().split(',')
                label = int(values[0])
                pixels = [0 if int(x) == 0 else 1 for x in values[1:]]
                self.digits.append(Digit(label, pixels))

    def compute_similarity(self, digit):
        for d in self.digits:
            d.set_similarity(digit)

    def most_similar(self):
        return sorted(self.digits, key = lambda x: x.similarity, reverse = True)[0]

    def find_k_most_similar(self, k):
        return sorted(self.digits, key = lambda x: x.similarity, reverse = True)[: k]

    def k_nearest_neighbors(self, k):
        return mode([x.label for x in self.find_k_most_similar(k)])

    def weighted_k_nearest_neighbors(self, k):
        k_neighbors = self.find_k_most_similar(k)
        weighted_votes = {}
        for rank, digit in enumerate(k_neighbors):
            weight = k - rank
            label = digit.get_label()
            weighted_votes[label] = weighted_votes.get(label, 0) + weight
        return max(weighted_votes, key=weighted_votes.get)

    def get_digits(self):
        return self.digits

    def print_digits(self):
        for digit in self.digits:
            print(f"Label: {digit.get_label()}\n")