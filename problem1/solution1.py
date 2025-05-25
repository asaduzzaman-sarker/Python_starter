def run_quiz(questions):
    score = 0
    total = len(questions)

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1} of {total}")
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n🎯 Quiz Completed!")
    print(f"Your Score: {score} out of {total}")


# List of questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 12", "C. 13", "D. 11"],
        "answer": "B"
    },
]

# Start quiz
run_quiz(quiz_questions)