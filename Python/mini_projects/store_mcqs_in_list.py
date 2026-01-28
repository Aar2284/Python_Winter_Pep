#      QUESTION

# Store 10 MCQ's in a list using loops

# Each question have 4 options (A, B, C ,D) stored in a named list
# Store the correct answers for all questions in separate list
# Display each question along with its option one-by-one
# Ask the user to enter an answer (A/B/C/D) for each question

# Problem input validation
# if user enter anything other than (A,B,C,D), display "invalid Enter A/B/C/D" and ask th same question again
# if answer is correct award 1 mark
# if answer is incorrect give 0 mark
# use loops to repeat the entire process till 10th question
# after all answer are done show the final marking out of 10

#       ANSWER


questions = [
    "What is the output of print(2 ** 3)?",
    "Which keyword is used to define a function in Python?",
    "How do you start a comment in Python?",
    "Which data type is immutable in Python?",
    "What does len('hello') return?",
    "Which method adds an element to the end of a list?",
    "What is the result of 10 // 3?",
    "Which operator is used for string concatenation?",
    "How do you check the data type of a variable?",
    "Which of these is NOT a valid variable name?"
]

options = [
    ["6", "8", "9", "12"],
    ["func", "def", "function", "define"],
    ["//", "/*", "#", "<!--"],
    ["List", "Dictionary", "Set", "Tuple"],
    ["4", "5", "6", "Error"],
    ["push()", "add()", "append()", "insert()"],
    ["3.33", "3", "3.0", "1"],
    ["&", "+", ".", ","],
    ["typeof()", "type()", "check()", "id()"],
    ["my_var", "_var", "2var", "var2"]
]

correct_answers = ['B', 'B', 'C', 'D', 'B', 'C', 'B', 'B', 'B', 'C']

score = 0
total_questions = len(questions)

print("Starting the Quiz...")
print("-" * 40)

for i in range(total_questions):
    print(f"\nQuestion {i + 1}: {questions[i]}")
    
    current_opts = options[i]
    print(f"A. {current_opts[0]}")
    print(f"B. {current_opts[1]}")
    print(f"C. {current_opts[2]}")
    print(f"D. {current_opts[3]}")
    
    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if user_answer in ['A', 'B', 'C', 'D']:
            
            if user_answer == correct_answers[i]:
                score += 1
            break  
        else:
            print("Invalid input! Enter A/B/C/D")

print("-" * 40)
print("Quiz Finished!")
print(f"Your Score: {score} out of {total_questions}")
