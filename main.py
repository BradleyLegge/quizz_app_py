import json
file_path = "q_and_a.json"

TOTAL_QUESTIONS = 15

def get_file_data():
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return questions

def user_validation():
   try:
       user_input = input("Enter your choice: ==> ").lower().strip()

       if user_input not in ["a", "b", "c", "d"]:
           raise ValueError("Invlaid choice. Please enter a valid choice.")
       return user_input
   except ValueError as e:
       print(e)
       return user_validation()

def main():
    questions = get_file_data()
    score = 0
    
    for question in questions:
        print(question["question"])
        print(question["choices"])
        user_input = user_validation()

        if user_input == question["answer"][0]:
            print("Correct!\n")
            score += 1
        else: print(f"Incorrect, the right answer is {question["answer"][0]}. {question["answer"][1]}.\n")

    print(f"You got {score} out of {TOTAL_QUESTIONS} correct!")
    print(f"Your score is {(score/TOTAL_QUESTIONS)*100:.2f}")

if __name__ == "__main__":
    main()