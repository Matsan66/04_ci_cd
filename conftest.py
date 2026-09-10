import pytest

from src.calculator import Calculator
from src.calculator_service import CalculatorService

@pytest.fixture
def test_calculator():
    return Calculator()

@pytest.fixture
def calculator_service(calculator):
    return CalculatorService(test_calculator)