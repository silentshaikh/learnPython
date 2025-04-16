import time
quiz_questions = [
    {
        "question": "What will be the output of `print(data[1]['name'])` if `data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]`?",
        "options": ["a) Alice", "b) Bob", "c) 25", "d) KeyError"],
        "answer": "b"
    },
    {
        "question": "What wiSll be printed after executing `users.append({'username': 'mark_smith'})` if `users = [{'username': 'john_doe'}, {'username': 'jane_doe'}]`?",
        "options": ["a) 2", "b) 3", "c) 4", "d) TypeError"],
        "answer": "b"
    },
    {
        "question": "After executing `students[0]['score'] = 85`, what will be the new value of `students[0]['score']` if `students = [{'id': 1, 'score': 80}, {'id': 2, 'score': 90}]`?",
        "options": ["a) 80", "b) 85", "c) 90", "d) KeyError"],
        "answer": "b"
    },
    {
        "question": "What will be printed if `keys = list(data[0].keys())` where `data = [{'brand': 'Apple', 'model': 'iPhone'}, {'brand': 'Samsung', 'model': 'Galaxy'}]`?",
        "options": ["a) ['Apple', 'iPhone']", "b) ['brand', 'model']", "c) ['Samsung', 'Galaxy']", "d) TypeError"],
        "answer": "b"
    },
    {
        "question": "What will `print('price' in products[0])` return if `products = [{'id': 101, 'name': 'Laptop'}, {'id': 102, 'name': 'Mouse'}]`?",
        "options": ["a) True", "b) False", "c) None", "d) KeyError"],
        "answer": "b"
    },
    {
        "question": "What will `print(high_earners)` output if `employees = [{'name': 'Alice', 'salary': 5000}, {'name': 'Bob', 'salary': 4000}, {'name': 'Charlie', 'salary': 6000}]` and `high_earners = [e['name'] for e in employees if e['salary'] > 4500]`?",
        "options": ["a) ['Alice', 'Charlie']", "b) ['Bob', 'Charlie']", "c) ['Alice']", "d) ['Charlie']"],
        "answer": "a"
    },
    {
        "question": "What will `print(students[0]['name'])` output if `students = [{'name': 'Emma', 'age': 22}, {'name': 'Liam', 'age': 20}]` and `students.sort(key=lambda x: x['age'])`?",
        "options": ["a) Emma", "b) Liam", "c) {'name': 'Liam', 'age': 20}", "d) TypeError"],
        "answer": "b"
    },
    {
        "question": "What will `print(user['name'])` output if `users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]` and `user = next((u for u in users if u['id'] == 2), None)`?",
        "options": ["a) Alice", "b) Bob", "c) None", "d) KeyError"],
        "answer": "b"
    },
    {
        "question": "How many elements will remain after filtering out completed tasks using `tasks = [t for t in tasks if not t['done']]` if `tasks = [{'task': 'Clean', 'done': False}, {'task': 'Cook', 'done': True}]`?",
        "options": ["a) 0", "b) 1", "c) 2", "d) KeyError"],
        "answer": "b"
    },
    {
        "question": "What will `print(len(merged))` output if `list1 = [{'id': 1, 'name': 'A'}]`, `list2 = [{'id': 2, 'name': 'B'}]`, and `merged = list1 + list2`?",
        "options": ["a) 1", "b) 2", "c) 3", "d) TypeError"],
        "answer": "b"
    }
]

correct = 0
totalPoint = 0

print("------ Welcome to our Quiz App ------")
print('------ Each Quiz == 5 marks ------')

# Start timer
start_time = time.time()
# index for go to the next quiz
quizCount = 0

while quizCount<len(quiz_questions):

    # print the question
    print(f"\n {quizCount+1}) {quiz_questions[quizCount]['question']}\n")

    #print the options of the question
    for option in quiz_questions[quizCount]['options']:
        print(option)

      # Calculate elapsed time
    elapsed_time = int(time.time() - start_time)
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60

    # Timer Start
    print(f"\n⏳ Timer: {minutes:02d} Min {seconds:02d} Sec\n")

    # Input for user answer
    userAnswer = input("\nEnter Your Answer (A | B | C | D) : ")
    # if answer is empty
    if not userAnswer:
        print("\nPlease enter the answer  \n")
    else:
        # if user answer is equal to the correct answer of question
        if userAnswer.lower() ==  quiz_questions[quizCount]['answer'].lower():
                # increment by 1 when an answer of the question is correct
                correct +=1
                # increment by 1 when an answer of the question is correct
                totalPoint+=5
        
        # increment by 1 when each question is complete
        quizCount +=1
   

# Stop timer
end_time = time.time()
total_time = int(end_time - start_time)
minutes = total_time // 60
seconds = total_time % 60

print(f"\n Your Quiz has completed \n")
print(f"Your Correct Answer is {correct} out of {len(quiz_questions)}")
print(f"\n Total Point is {totalPoint}")
print(f"\n⏱️ Total Time Taken: {minutes:02d} Min {seconds:02d} Sec")
