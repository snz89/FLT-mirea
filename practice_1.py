def parse_expression(expression):
    result = []
    current_number = ""

    for char in expression:
        if char.isdigit():
            current_number += char
        elif char != " ":
            if current_number:
                result.append(int(current_number))
                current_number = ""
            result.append(char)

    if current_number:
        result.append(int(current_number))

    return result


def infix_to_postfix(expression):
    def operand_priority(c):
        if c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1

    result = []
    stack = []

    for token in expression:
        if isinstance(token, int) or isinstance(token, float):
            result.append(str(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and operand_priority(token) <= operand_priority(stack[-1]):
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return result


def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack.pop()


def prac1(expression):
    return evaluate_postfix(infix_to_postfix(parse_expression(expression)))


if __name__ == "__main__":
    print(f"ожидаемый ответ: 10, ответ: {prac1('10 * (2 - 1)')}")
    print(f"ожидаемый ответ: 26, ответ: {prac1('10 / 2 + 8 * 3 - (1 + 2)')}")
