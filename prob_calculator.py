import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():
            self.contents += v * [k]

    def draw(self, num):
        num = min(num, len(self.contents))
        balls = []
        for x in range(num):
            ind = random.randint(0, len(self.contents)-1)
            balls.append(self.contents.pop(ind))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        a_hat = copy.deepcopy(hat)
        balls = a_hat.draw(num_balls_drawn)
        right_colors = 0
        for color in expected_balls.keys():
            if balls.count(color) >= expected_balls[color]:
                right_colors += 1
        if right_colors == len(expected_balls):
            M += 1
    probability = float(M) / num_experiments
    return probability