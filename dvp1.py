def get_valid_test_score():
    while True:
        try:
            score = float(input("Enter the test marks: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


test_scores = []
for i in range(3):
    test_scores.append(get_valid_test_score())
test_scores.sort(reverse=True)
best_two_average_score = sum(test_scores[:2]) / 2
print(f"The average of the best two test scores is: {best_two_average_score}")