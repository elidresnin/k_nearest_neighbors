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
        '''
        totalSame = 28 * 28
        for i in range(28):
            filledFirst = 0
            filledSecond = 0
            for j in range(28):
                if self.pixels[i][j] == 1:
                    filledFirst += 1
                if  self.pixels[j][i] == 1:
                    filledFirst += 1
                if other.pixels[i][j] == 1:
                    filledSecond += 1
                if other.pixels[j][i] == 1:
                    filledSecond += 1
            totalSame -= abs(filledFirst - filledSecond)
        self.similarity = totalSame/(2*28*28)
        '''
        total = 0
        for i in range(28):
            for j in range(28):
                if self.pixels[i][j] == other.pixels[i][j]:
                    total += 1
        self.similarity = total/(28*28)


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
        display = f"label = {self.label} \n"
        display += f"similarity = {self.get_similarity()} \n|"
        display += "-" * 28 + "|\n|"
        for row in self.pixels:
            for p in row:
                display += ' ' if p == 0 else '*'
            display += "|\n|"
        display += "_" * 28 + "|\n"
        return display