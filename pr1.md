Этот код реализует калькулятор для выражений в инфиксной нотации (например, `10 * (2 - 1)`), который сначала преобразует выражение в постфиксную нотацию (также известную как обратная польская запись, ОПЗ), а затем вычисляет результат. Давайте разберем его более детально:

### 1. Функция `parse_expression(expression)`

**Цель**: Разделить строку с математическим выражением на отдельные токены (числа и операторы).

```python
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
```

- Проходится по каждому символу строки.
- Если символ — цифра, он добавляется к текущему числу `current_number`.
- Если встречается оператор (например, `+`, `-`, `*`, `/`) или скобка, текущее число преобразуется в целое и добавляется в результат, а затем добавляется сам оператор.
- В конце, если осталось число в `current_number`, оно добавляется в список.
- Возвращает список токенов, где числа представлены как `int`, а операторы и скобки — как строки.

**Пример**:
```python
parse_expression("10 * (2 - 1)")  # Результат: [10, '*', '(', 2, '-', 1, ')']
```

### 2. Функция `infix_to_postfix(expression)`

**Цель**: Преобразовать выражение в инфиксной нотации (обычная запись) в постфиксную нотацию (ОПЗ).

```python
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
            while stack and operand_priority(token) < operand_priority(stack[-1]):
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return result
```

- Использует стек для хранения операторов и их приоритетов.
- Числа сразу добавляются в результат.
- Открывающие скобки `(` добавляются в стек, закрывающие `)` вызывают перенос всех операторов до ближайшей открывающей скобки в результат.
- Операторы `+`, `-`, `*`, `/` добавляются в стек с учетом приоритета, и при необходимости операторы из стека переносятся в результат.
- В конце все операторы, оставшиеся в стеке, добавляются в результат.

**Пример**:
```python
infix_to_postfix([10, '*', '(', 2, '-', 1, ')'])  # Результат: ['10', '2', '1', '-', '*']
```

### 3. Функция `evaluate_postfix(expression)`

**Цель**: Вычислить значение выражения в постфиксной нотации.

```python
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
```

- Числа добавляются в стек.
- Когда встречается оператор, извлекаются два последних числа из стека, выполняется операция, и результат снова помещается в стек.
- После обработки всех токенов в стеке остается одно значение — результат.

**Пример**:
```python
evaluate_postfix(['10', '2', '1', '-', '*'])  # Результат: 10
```

### 4. Основная функция `prac1(expression)`

**Цель**: Связать все три шага вместе.

```python
def prac1(expression):
    return evaluate_postfix(infix_to_postfix(parse_expression(expression)))
```

- Принимает выражение в инфиксной нотации.
- Сначала разбирает выражение на токены с помощью `parse_expression`.
- Затем преобразует в постфиксную запись с помощью `infix_to_postfix`.
- И наконец, вычисляет результат через `evaluate_postfix`.

### Пример использования:

```python
if __name__ == "__main__":
    print(f"ожидаемый ответ: 10, ответ: {prac1('10 * (2 - 1)')}")
    print(f"ожидаемый ответ: 26, ответ: {prac1('10 / 2 + 8 * 3 - (1 + 2)')}")
```

- Для выражения `'10 * (2 - 1)'`, результат будет 10.
- Для выражения `'10 / 2 + 8 * 3 - (1 + 2)'`, результат будет 26.

### Принцип работы:

1. **Разбор выражения**: Строка разбивается на числа и операторы.
2. **Преобразование в ОПЗ**: Инфиксная запись преобразуется в постфиксную, что упрощает вычисления.
3. **Вычисление результата**: Используя стек, производится последовательное вычисление выражения.
