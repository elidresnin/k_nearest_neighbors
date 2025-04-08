from DigitMatcher import DigitMatcher
from Digit import Digit
from PrintHelper import PrintHelper

class DigitMatcherRunner:
    @staticmethod
    def populate_array_of_test_digits(test_digits_file_path):

        test_digits = []

        try:
            with open(test_digits_file_path, 'r') as f:
                for line in f:
                    # Split the line into pixel values
                    values = line.strip().split(',')
                    label = int(values[0])
                    # Convert pixel values to integers (0 or 1)
                    pixels = [0 if int(x) == 0 else 1 for x in values]

                    # Create a Digit object with a dummy label (-1) since test data has no labels
                    test_digit = Digit(label, pixels)
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
        digit_collection = DigitMatcher("tiny_train.csv")
        #print(digit_collection.get_digits()[0])

        # Testing Activity 3
        print("Activity 3 - Compare two digits")
        firstDigit = digit_collection.get_digits()[1]
        secondDigit = digit_collection.get_digits()[5]
        firstDigit.set_similarity(secondDigit)
        #print(firstDigit)
        #print(secondDigit)

        # Get test digits
        test_digits = DigitMatcherRunner.populate_array_of_test_digits("tiny_test.csv")
        testDigit = test_digits[0]

        # Testing Activity 4
        print("Activity 4 - Find most similar")
        digit_collection.compute_similarity(testDigit)
        # print(firstDigit)
        print(digit_collection.most_similar())

        print("Activity 5 - Find kNN")
        k = 3
        kNN = digit_collection.find_k_most_similar(k)
        print("kNN digit's label is " + str(digit_collection.k_nearest_neighbors(k)))
        PrintHelper.print(firstDigit, kNN)
        # print(digit_collection.k_nearest_neighbors(3))


        print("Activity 6 - Weighted kNN")
        print("Weighted kNN digit's label is " + str(digit_collection.k_nearest_neighbors(k)))
        PrintHelper.print(firstDigit, kNN)

        print("\nActivity 7 - Test Accuracy")

        correct_predictions = 0
        total_tests = len(test_digits)

        for test_digit in test_digits:
            digit_collection.compute_similarity(test_digit)
            predicted_label = digit_collection.k_nearest_neighbors(k)
            true_label = test_digit.get_label()
            if predicted_label == true_label:
                correct_predictions += 1
            else:
                print("guessed label:" + str(predicted_label))
                print("correct label:" + str(true_label))

        accuracy = correct_predictions / total_tests
        print("Number of correct: " + str(correct_predictions))
        print("Number of incorrect: " + str(total_tests - correct_predictions))

        print(f"Accuracy using k = {k}: {accuracy:.2%}")

if __name__ == "__main__":
    DigitMatcherRunner.main()