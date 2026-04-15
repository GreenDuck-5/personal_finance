class SavingsTracker:
    def __init__(self):
        self.current = 0
        self.goal = 0

    def set_goal(self, amount):
        self.goal = float(amount)

    def add_savings(self, amount):
        self.current += float(amount)

    def progress(self):
        if self.goal > 0:
            return (self.current / self.goal) * 100
        return 0