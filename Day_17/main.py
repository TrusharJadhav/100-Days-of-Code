from data import question_data
from question_model import Question
from Quiz_brain import Quizbrain
question_bank=[]
for question in question_data:
    que=question["text"]
    ans=question["answer"]
    question_bank.append(Question(que,ans))

quiz=Quizbrain(question_bank)
quiz.next_question


