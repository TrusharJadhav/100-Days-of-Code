class Quizbrain:
    def __init__(self,q_list):
        self.question_number=0
        self.correct=0
        self.question_list=q_list
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        choice=input(f"Q{self.question_number}: {current_question.question} (true/false)?").lower()
        self.check_answer(choice,current_question.answer)
       
    def check_answer(self,choice,correct_answer):
        if choice==correct_answer.lower():
            print("You got it right !")
            self.correct+=1
        print(f"Correct answer was: {correct_answer}")
        print(f"Your current score is {self.correct}/{self.question_number}")
        print("\n")
    def still_has_question(self):
        return self.question_number<len(self.question_list)

