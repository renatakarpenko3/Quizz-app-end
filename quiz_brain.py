import html

class QuizBrain:

    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.questions = q_list
        self.current_q = None

    def still_has_questions(self):
        return self.q_num < len(self.questions)

    def next_question(self):
        self.current_q = self.questions[self.q_num]
        self.q_num += 1
        q_text = html.unescape(self.current_q.text)
        return f"Q.{self.q_num}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_q.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
