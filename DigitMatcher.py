from Digit import Digit

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
        # Needs implementation
        return None

    def k_nearest_neighbors(self, k):
        # Needs implementation
        return 0

    def weighted_k_nearest_neighbors(self, k):
        # Needs implementation
        return 0

    def get_digits(self):
        return self.digits

    def print_digits(self):
        for digit in self.digits:
            print(f"Label: {digit.get_label()}\n")