from Question import Question
question_prompt=[
    "What color are apples? \n (a) Red/Green \n (b) Orange \n (c) Purple \n",
    "What color are bananas? \n (a) Red/Green \n (b) Yellow \n (c) Purple \n",
    "What color are strawberries? \n (a) Green \n (b) Orange \n (c) Red \n"
]
questions=[
   Question(question_prompt[0],"a"),
   Question(question_prompt[1],"b"),
   Question(question_prompt[2],"c"),
]

def run_test(questions):
    score=0
    for question in questions:
        answers=input(question.prompt)
        if answers==question.answer:
            score+=1
    print("YOu got "+str(score)+"/"+str(len(questions))+" correct")
        
run_test(questions)