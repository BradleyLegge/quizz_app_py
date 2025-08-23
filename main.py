file_path = "q_and_a.txt"

TOTAL_QUESTIONS = 10
questions = {}
score = 0

try:
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(":", 1)
            questions[key.strip()] = value.strip()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(questions["question"])
print(questions["choices"])
user_input = input("Answer: ==> ")

# print(questions["answer"])

if user_input.lower() == questions["answer"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"{score} out of {TOTAL_QUESTIONS}")