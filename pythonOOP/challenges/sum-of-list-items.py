class Student:
    def __init__(self, scores):
        self.scores = scores

    def get_score_sum(self):
        result = sum(self.scores)
        return result


scores = [55, 75, 80, 62, 77]
s1 = Student(scores)
total = s1.get_score_sum()
print(total)