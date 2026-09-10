class CalculatorService:
    """
    Represents a calculator service.
    """
    def __init__(self, calculator):
        self.calculator = calculator

    def calculate(self, operation, a, b):
        """
        Returns the result of an operation on the two numbers.
        """
        match operation:
            case "add":
                return self.calculator.add(a, b)
            case "subtract":
                return self.calculator.subtract(a, b)
            case  "multiply":
                return self.calculator.multiply(a, b)
            case  "divide":
                return self.calculator.divide(a, b)
            case _:
                raise ValueError("Invalid operation")
