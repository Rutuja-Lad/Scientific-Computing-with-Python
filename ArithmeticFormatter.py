def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists for the top row, bottom row, dashes, and answers
    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        # Split each problem into operands and operator
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        num1, operator, num2 = parts

        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate that operands are digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Validate that operands are not more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the result if needed
        if operator == '+':
            result = str(int(num1) + int(num2))
        elif operator == '-':
            result = str(int(num1) - int(num2))

        # Determine the width of the problem
        width = max(len(num1), len(num2)) + 2  # Account for operator and space

        # Format each row of the problem
        top_row.append(f"{num1:>{width}}")
        bottom_row.append(f"{operator} {num2:>{width - 2}}")
        dashes.append('-' * width)
        if show_answers:
            answers.append(f"{result:>{width}}")

    # Combine rows into final output
    arranged_problems = '    '.join(top_row) + '\n' + '    '.join(bottom_row) + '\n' + '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems



    

print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
