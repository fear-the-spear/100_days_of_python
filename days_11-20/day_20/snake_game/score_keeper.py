class ScoreKeeper:
    def __init__(self):
        self.scores = []

    def record_score(self, user_name, score):
        self.file = open("scores_record.py", "w")
        self.file.write(f"{user_name}: {score}")
        self.file.close()
