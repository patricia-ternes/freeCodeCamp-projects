# Code by freeCodeCamp
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
hat.draw(5)
print(hat.contents)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2, "red": 1},
    num_balls_drawn=4,
    num_experiments=3000,
)
print("Probability:", probability)

# Run unit tests automatically
main(module="test_module", exit=False)

hat = prob_calculator.Hat(red=5, blue=2)
actual = hat.draw(2)
print(actual)
