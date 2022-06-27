# Solution by Patricia Ternes <patricia.terdal@gmail.com>
# https://github.com/patricia-ternes/tree/main/freeCodeCamp-projects/Arithmetic-Formatter/ScientificComputingPython/arithmetic_arranger.py
def arithmetic_arranger(problems, solution=False):
    N = len(problems)

    # Check the limit (five) of problems supplied to the function.
    if N > 5:
        return "Error: Too many problems."

    operand1 = [problem.split()[0] for problem in problems]
    operand2 = [problem.split()[2] for problem in problems]
    operator = [problem.split()[1] for problem in problems]

    # Check incorrect operators
    if not all(item in ["+", "-"] for item in operator):
        return "Error: Operator must be '+' or '-'."

    # Check if all operands are digitis
    if not all([item.isdigit() for item in operand1 + operand2]):
        return "Error: Numbers must only contain digits."

    # Check operands length
    if not all([len(item) < 5 for item in operand1 + operand2]):
        return "Error: Numbers cannot be more than four digits."

    # Determine solution (if necessary)
    if solution:
        operation = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y)}
        solutions = [
            operation[operator[i]](int(operand1[i]), int(operand2[i])) for i in range(N)
        ]

    # Print formatting
    ## There should be a single space between the operator and the longest of the two
    length = [2 + max(len(operand1[i]), len(operand2[i])) for i in range(N)]

    ## Numbers should be right-aligned.
    operand1 = [operand1[i].rjust(length[i]) for i in range(N)]

    ## Operator will be on the same line as the second operand
    operand2 = [
        "".join([operator[i], operand2[i].rjust(length[i] - 1)]) for i in range(N)
    ]

    ## There should be dashes at the bottom of each problem.
    ## The dashes should run along the entire length of each problem individually.
    dashes = [item * "-" for item in length]

    ## There should be four spaces between each problem.
    space = 4 * " "
    arranged_problems = "\n".join(
        [space.join(operand1), space.join(operand2), space.join(dashes)]
    )

    ## When the second argument is set to True, the answers should be displayed
    if solution:
        solutions = [str(solutions[i]).rjust(length[i]) for i in range(N)]
        arranged_problems = "\n".join([arranged_problems, space.join(solutions)])

    return arranged_problems
