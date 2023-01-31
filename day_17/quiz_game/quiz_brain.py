class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number <= len(self.question_list) - 1

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong, it's actually {correct_answer}.")
        print(f"Current Score: {self.score}/{self.question_number}\n")

    def print_final_score(self):
        self.list_length = len(self.question_list)
        if self.question_number == self.list_length:
            print("You completed the quiz!")
            print(
                f"You correctly answered {self.score} out of {self.list_length} ({round((self.score / self.list_length), 3) * 100}%)")
