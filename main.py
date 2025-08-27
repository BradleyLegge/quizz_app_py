import json

file_path = "q_and_a.json"

TOTAL_QUESTIONS = 3
questions = {}
score = 0

try:
    with open(file_path, 'r') as file:
        questions = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

for question in questions:
    print(question["question"])
    print(question["choices"])
    user_input = input("Choice your answer: ==> ")

    if user_input == question["answer"]:
        print("Correct!")
        score += 1
    else: print("Incorrect")

print(f"You got {score} out of {TOTAL_QUESTIONS} correct!")
print(f"Your score is {(score/TOTAL_QUESTIONS)*100:.2f}")