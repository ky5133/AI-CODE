import requests 

url="https://opentdb.com/api.php?amount=15&category=12&difficulty=easy&type=multiple"

response=requests.get(url)

if response.status_code==200:
    trivia_data=response.json()
    score=0



    for i, question_data in enumerate (trivia_data["results"]):
        print(f"Question {i + 1}: {question_data['question']}")
        options=[question_data['correct_answer']]+question_data['incorrect_answers']
        option=sorted(options)
        for j, option in enumerate(options):
            print(f"{j+1}.{option}")

        user_answer=input("Your answer(1/2/3/4):")
        if options[int(user_answer)-1]==question_data["correct_answer"]:
            print("Correct!")
            score =+ 1

        else:
            print(f"Wrong!The correct answer was:{question_data['correct_answer']}")

        print("/n")

    print(f"your final score:{score}/{len(trivia_data['results'])}")

else:
    print("fail to retrieve trivia")
