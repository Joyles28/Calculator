first_operand = None
second_operand = None
operator = None
result = None

def calculate(first_operand, second_operand, operator, result):

    try:
        if operator == "+":
            result = float(first_operand) + float(second_operand)
        elif operator == "-":
            result = float(first_operand) - float(second_operand)
        elif operator == "*":
            result = float(first_operand) * float(second_operand)
        elif operator == "/":
            result = float(first_operand) / float(second_operand)

        first_operand = f"{result:.2f}"
    except ZeroDivisionError:
        first_operand = None
    second_operand = None
    operator = None
    result = None


