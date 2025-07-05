import random

class DrinkingGame:
    def __init__(self):
        self.challenges = [
            "Take a shot",
            "Pass the drink",
            "Make a toast",
            "Double dare",
            "Take two sips",
            "Tell a joke",
            "Sing a song"
        ]

    def spin(self):
        return random.choice(self.challenges)