import pytest


@pytest.mark.integrationtest
def test_calculator_service_integration_add(calculator_service):
    """
    Tests the addition of two numbers.
    :param calculator_service: A CalculatorService fixture instance.
    """
    # Act
    result = calculator_service.calculate("add", 2, 3)
    # Assert
    assert result == 5


@pytest.mark.integrationtest
def test_calculator_service_integration_subtract(calculator_service):
    """
    Tests the subtraction of two numbers.
    :param calculator_service: A CalculatorService fixture instance.
    """
    # Act
    result = calculator_service.calculate("subtract", 5, 3)
    # Assert
    assert result == 2


@pytest.mark.integrationtest
def test_calculator_service_integration_multiply(calculator_service):
    """
    Tests the multiplying of two numbers.
    :param calculator_service: A CalculatorService fixture instance.
    """
    # Act
    result = calculator_service.calculate("multiply", 4, 3)
    # Assert
    assert result == 12


@pytest.mark.integrationtest
def test_calculator_service_integration_divide(calculator_service):
    """
    Tests the division of two numbers.
    :param calculator_service: A CalculatorService fixture instance.
    """
    # Act
    result = calculator_service.calculate("divide", 10, 2)
    # Assert
    assert result == 5


@pytest.mark.integrationtest
def test_calculator_service_integration_invalid_operation(calculator_service):
    """
    Tests invalid operations.
    :param calculator_service: A CalculatorService fixture instance.
    """
    # Act/ assert
    with pytest.raises(ValueError, match="Invalid operation"):
        calculator_service.calculate("invalid", 5, 3)
