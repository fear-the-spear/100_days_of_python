from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    q_obj = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(q_obj)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

quiz.print_final_score()
