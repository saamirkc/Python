original_word="samir"
guess=""
guess_count=0

while guess!=original_word and guess_count<3:
   guess=input("Enter your guess :")
   guess_count+=1
if guess==original_word:
    print("You won!")
else:
    print("YOu Loose")