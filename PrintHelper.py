class PrintHelper:
    @staticmethod
    def print(test_digit, k_digits):
        digit_strings = test_digit.get_pixels_for_printing()
        for d in k_digits:
            for row in range(len(digit_strings)):
                digit_strings[row] += d.get_pixels_for_printing()[row]
        for s in digit_strings:
            print(s)