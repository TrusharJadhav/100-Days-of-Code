# Quiz Game
from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
import random
question_bank=[]
for question in question_data:
    que=question["question"]
    ans=question["correct_answer"]
    question_bank.append(Question(que,ans))
random.shuffle(question_bank)
quiz=Quizbrain(question_bank)

while quiz.still_has_question():
    score=quiz.next_question()
print(f"You have completed the quiz \nYour final score is {quiz.correct}/{quiz.question_number+1}")



