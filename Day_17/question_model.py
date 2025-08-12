class Question():
    def __init__(self,text,answer):
        self.question=text
        self.answer=answer

new_q=Question("2+3=5",True)
print(new_q.question)