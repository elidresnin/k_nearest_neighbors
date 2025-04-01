from DigitMatcher import DigitMatcher
from Digit import Digit

class DigitMatcherRunner:
    @staticmethod
    def populate_array_of_test_digits(test_digits_file_path):

        test_digits = []

        try:
            with open(test_digits_file_path, 'r') as f:
                for line in f:
                    # Split the line into pixel values
                    values = line.strip().split(',')

                    # Check if we have the expected number of pixels (784 for 28x28)
                    if len(values) != 784:
                        raise ValueError(f"Expected 784 pixel values, got {len(values)}")

                    # Convert pixel values to integers (0 or 1)
                    pixels = [0 if int(x) == 0 else 1 for x in values]

                    # Create a Digit object with a dummy label (-1) since test data has no labels
                    test_digit = Digit(-1, pixels)
                    test_digits.append(test_digit)

            return test_digits

        except FileNotFoundError:
            print(f"Error: Test file '{test_digits_file_path}' not found")
            return []
        except ValueError as e:
            print(f"Error in file format: {str(e)}")
            return []

    @staticmethod
    def main():
        # Test Activity 2
        print("Activity 2 - Read digits from an input file")
        digit_collection = DigitMatcher("small_train.csv")
        print(digit_collection.get_digits()[0])

        # Testing Activity 3
        print("Activity 3 - Compare two digits")
        digit_collection.get_digits()[1].set_similarity(digit_collection.get_digits()[0])
        print(digit_collection.get_digits()[0])
        print(digit_collection.get_digits()[1])

if __name__ == "__main__":
    DigitMatcherRunner.main()