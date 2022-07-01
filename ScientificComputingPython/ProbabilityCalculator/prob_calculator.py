# Solution by Patricia Ternes <patricia.terdal@gmail.com>
# https://github.com/patricia-ternes/freeCodeCamp-projects/blob/main/ScientificComputingPython/ProbabilityCalculator/prob_calculator.py

import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, n):
        if len(self.contents) < n:
            return self.contents

        drawn = random.sample(self.contents, n)
        [self.contents.remove(item) for item in drawn]
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0.0
    for i in range(num_experiments):
        drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        j = all([drawn.count(key) >= value for key, value in expected_balls.items()])

        if j:
            M += 1.0

    return M / num_experiments
