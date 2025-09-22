def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # set up lists for formatting, like in Polygon project
    top_numbers = []
    operator_lines = []
    dash_lines = []
    answer_numbers = []
    # split each problem, inspired by Cipher splitting
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid format.'
        first_num, operator, second_num = parts
        if not (operator == '+' or operator == '-'):
            return "Error: Operator must be '+' or '-'."
        if len(first_num) > 4 or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not (first_num.isdigit() and second_num.isdigit()):
            return 'Error: Numbers must only contain digits.'
        # calculate width, learned from alignment in Case Converter
        width = max(len(first_num), len(second_num)) + 2
        top_numbers.append(first_num.rjust(width))
        operator_lines.append(operator + ' ' + second_num.rjust(width - 2))
        dash_lines.append('-' * width)
        if show_answers:
            if operator == '+':
                ans = str(int(first_num) + int(second_num))
            else:
                ans = str(int(first_num) - int(second_num))
            answer_numbers.append(ans.rjust(width))
    formatted = ' '.join(top_numbers) + '\n' + ' '.join(operator_lines) + '\n' + ' '.join(dash_lines)
    if show_answers:
        formatted += '\n' + ' '.join(answer_numbers)
    return formatted
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
