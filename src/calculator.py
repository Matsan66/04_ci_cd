class Calculator:
    """
    Represents a calculator.
    """

    def add(self, a, b):
        """
        Returns the sum of two numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Returns the difference of two numbers.
        """
        return a - b

    def multiply(self, a, b):
        """
        Returns the product of two numbers.
        """
        return a * b

    def divide(self, a, b):
        """
        Returns the quotient of two numbers. Throws ValueError if division by zero.
        """
        if b == 0:
            raise ValueError("Divide by zero not allowed")
        return a / b
