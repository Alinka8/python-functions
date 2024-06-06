questions = [
    'What is the city of Kyrgyzstan?',
    'Is George Washington the first President of the United States? (True/False)',
    'Who is the CEO of Google?',
    'What is 8 divided by 4?'
]

def quiz():
    global questions
    correct_answers = ['Bishkek', True, 'Sundar Pichai', 2]
    answer_types = [str, bool, str, int]
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i] + ' ')
        try:
            if answer_types[i] == bool:
                converted_answer = user_answer.lower() in ['true', '1', 'yes', 'y']
            else:
                converted_answer = answer_types[i](user_answer)
                
            if converted_answer == correct_answers[i]:
                print("Correct")
                score += 1
            else:
                print('Wrong Answer')
        except ValueError:
            print('Wrong Answer')
    print(f"Your final score is {score}/{len(questions)}")

quiz()
