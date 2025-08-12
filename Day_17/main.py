from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
Question_bank=[]
for q in question_data:
    text=q["text"]
    ans=q["answer"]
    new_questiom=Question(text,ans)
    Question_bank.append(new_questiom)
quiz=Quizbrain(Question_bank)


print(Question_bank[0].question)
quiz.next_question()