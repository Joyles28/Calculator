result = None

def calculate():
    global first_operand, second_operand, operator, result

    text = f"{first_operand} {operator} {second_operand} = "
    
    try:
        if operator == "+":
            result = float(first_operand) + float(second_operand)
        elif operator == "-":
            result = float(first_operand) - float(second_operand)
        elif operator == "*":
            result = float(first_operand) * float(second_operand)
        elif operator == "/":
            result = float(first_operand) / float(second_operand)

        result = f"{result:.2f}"
    except ZeroDivisionError:
        result = "Undefined"
        
    text += result
    
    return text

