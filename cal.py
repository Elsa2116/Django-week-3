def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation.")
        
        print(f"Result: {result}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
calculator()