import pytest

@pytest.mark.parametrize(
    # Adds test parameters for all addition tests
    # Arrange
    "a, b, expected",
    [
        pytest.param(2, 3, 5, id="positive_numbers"),
        pytest.param(-2, -3, -5, id="negative_numbers"),
        pytest.param(5, -3, 2, id="positive_and_negative numbers"),
        pytest.param(0, 5, 5, id="zero_number_first"),
        pytest.param(5, 0, 5, id="zero_number_second"),
        pytest.param(0, 0, 0, id="both_numbers_zero"),
        pytest.param(1000000, 2000000, 3_000_000, id="large_numbers"),
        pytest.param(1.5, 2.5, 4.0, id="decimal_numbers"),
    ],
)

@pytest.mark.unittest
def test_calculator_add(a, b, expected, test_calculator):
    """
    Tests that the calculator correctly adds two numbers.
    :param test_calculator: A calculator fixture
    """
    # Act
    result = test_calculator.add(a, b)

    # Assert
    assert result == expected

# ------------------------------------------------------------------------

@pytest.mark.parametrize(
    # Adds test parameters for all subtraction tests
    # Arrange
    "a, b, expected",
    [
        pytest.param(5, 3, 2, id="positive_numbers"),
        pytest.param(-2, -3, 1, id="negative_numbers"),
        pytest.param(3, 5, -2, id="result_is_negative"),
        pytest.param(5, -3, 8, id="positive_minus_negative"),
        pytest.param(-5, 3, -8, id="negative_minus_positive"),
        pytest.param(0, 5, -5, id="zero_first"),
        pytest.param(5, 0, 5, id="zero_second"),
        pytest.param(0, 0, 0, id="both_numbers_zero"),
        pytest.param(1000000, 500000, 500000, id="large_numbers"),
        pytest.param(5.5, 2.5, 3.0, id="decimal_numbers"),
    ],
)

@pytest.mark.unittest
def test_calculator_subtract(a, b, expected, test_calculator):
    """
    Tests that the calculator correctly subtracts two numbers.
    :param test_calculator: A calculator fixture
    """
    # Act
    result = test_calculator.subtract(a, b)

    # Assert
    assert result == expected


# ------------------------------------------------------------------------


@pytest.mark.parametrize(
    # Adds test parameters for all addition tests
    # Arrange
    "a, b, expected",
    [
        pytest.param(2, 3, 6, id="positive_numbers"),
        pytest.param(-2, -3, 6, id="negative_numbers"),
        pytest.param(3, -5, -15, id="positive_times_negative"),
        pytest.param(-3, 5, -15, id="negative_times_positive"),
        pytest.param(0, 5, 0, id="zero_first"),
        pytest.param(5, 0, 0, id="zero_second"),
        pytest.param(0, 0, 0, id="both_numbers_zero"),
        pytest.param(1000, 2000, 2000000, id="large_numbers"),
        pytest.param(1.5, 2.5, 3.75, id="decimal_numbers"),
    ],
)

@pytest.mark.unittest
def test_multiply(a, b, expected, test_calculator):
    """
    Tests that the calculator correctly multiplies two numbers.
    :param test_calculator: A calculator fixture
    """
    # Act
    result = test_calculator.multiply(a, b)

    # Assert
    assert result == expected


# ------------------------------------------------------------------------


@pytest.mark.parametrize(
    # Arrange
    "a, b, expected",
    [
        pytest.param(6, 3, 2, id="positive_numbers"),
        pytest.param(-6, -3, 2, id="negative_numbers"),
        pytest.param(6, -3, -2, id="positive_divided_by_negative"),
        pytest.param(-6, 3, -2, id="negative_divided_by_positive"),
        pytest.param(0, 5, 0, id="zero_first"),
        pytest.param(10, 2, 5, id="even_division"),
        pytest.param(5, 2, 2.5, id="decimal_result"),
        pytest.param(1_000_000, 2_000, 500, id="large_numbers"),
        pytest.param(5.5, 2.0, 2.75, id="decimal_numbers"),
    ],
)

@pytest.mark.unittest
def test_divide(a, b, expected, test_calculator):
    """
    Tests that the calculator correctly divides two numbers.
    :param test_calculator: A calculator fixture
    """
    # Act
    result = test_calculator.divide(a, b)

    # Assert
    assert result == expected

@pytest.mark.unittest
def test_divide_by_zero(test_calculator):
    """
    Tests that the calculator correctly throws a ValueError exception if division by zero.
    :param test_calculator: A calculator fixture
    """
    # Prepare
    number_a = 10
    number_b = 0

    # Act & Assert
    with pytest.raises(ValueError, match="Divide by zero not allowed"):
        test_calculator.divide(number_a, number_b)