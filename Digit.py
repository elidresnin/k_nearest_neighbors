class Digit:
    def __init__(self, label, pixels):
        self.label = label
        self.pixels = [[0 for _ in range(28)] for _ in range(28)]
        self.similarity = 0.0
        self._construct_pixels(pixels)

    def _construct_pixels(self, pixels):
        for i in range(28):
            for j in range(28):
                self.pixels[i][j] = pixels[i * 28 + j]

    def get_pixels(self):
        return self.pixels

    def get_label(self):
        return self.label

    def set_similarity(self, other):
        pass

    def get_similarity(self):
        return self.similarity

    def get_pixels_for_printing(self):
        print_pixels = []
        current_string = ""
        for c in str(self):
            if c != '\n':
                current_string += c
            else:
                print_pixels.append(current_string)
                current_string = ""
        return print_pixels

    def __str__(self):
        display = f"label = {self.label}                     \n"
        display += "similarity = {:.13f}   \n|" if self.get_similarity() > 0 else "                              \n|"
        display += "-" * 28 + "|\n|"
        for row in self.pixels:
            for p in row:
                display += ' ' if p == 0 else '*'
            display += "|\n|"
        display += "_" * 28 + "|\n"
        return display