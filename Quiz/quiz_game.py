import random
print("Welcome to python quiz app")
option=input("Do you want to play?(y/n) ")
if option !="y":
    quit()
else:
    name=input("Enter your name: ")
    print(f"Lets play this quiz game {name} ")
    questions = [
        {
            "question": "What is the capital of Japan?",
            "options": ["A) Tokyo", "B) Beijing", "C) Seoul", "D) Bangkok"],
            "correct_answer": "A) Tokyo"
        },
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Rome"],
            "correct_answer": "A) Paris"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["A) Mars", "B) Venus", "C) Jupiter", "D) Saturn"],
            "correct_answer": "A) Mars"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "correct_answer": "A) H2O"
        },
    {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
            "correct_answer": "B) William Shakespeare"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Carbon dioxide", "C) Nitrogen", "D) Hydrogen"],
            "correct_answer": "B) Carbon dioxide"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Tiger"],
            "correct_answer": "C) Blue Whale"
        },
        {
            "question": "Which gas makes up the majority of Earth's atmosphere?",
            "options": ["A) Oxygen", "B) Carbon dioxide", "C) Nitrogen", "D) Hydrogen"],
            "correct_answer": "C) Nitrogen"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
            "correct_answer": "C) Au"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Leonardo da Vinci", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Michelangelo"],
            "correct_answer": "A) Leonardo da Vinci"
        },
        {
            "question": "Which gas do humans exhale when they breathe out?",
            "options": ["A) Oxygen", "B) Carbon dioxide", "C) Nitrogen", "D) Hydrogen"],
            "correct_answer": "B) Carbon dioxide"
        }
    ]

    # Shuffle the questions to make the quiz random
    random.shuffle(questions)

    # Initialize the score
    score = 0

    # Quiz loop
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q['correct_answer'][0]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['correct_answer']}\n")

    # Display the final score
    print(f"{name}, your final score is: {score}/{len(questions)}")
