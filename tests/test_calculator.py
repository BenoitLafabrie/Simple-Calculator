import pytest
from src.calculator import Calculator

class TestCalculator:
    
    def test_addition_positive_numbers(self):
        result = Calculator.add(5, 3)
        assert result == 8
    
    def test_addition_negative_numbers(self):
        result = Calculator.add(-5, -3)
        assert result == -8
        
    def test_addition_mixed_numbers(self):
        result = Calculator.add(-5, 3)
        assert result == -2
    
    def test_addition_decimals(self):
        result = Calculator.add(2.5, 3.7)
        assert result == pytest.approx(6.2)
    
    def test_subtraction_basic(self):
        result = Calculator.subtract(10, 4)
        assert result == 6
    
    def test_subtraction_negative_result(self):
        result = Calculator.subtract(3, 7)
        assert result == -4
    
    def test_multiplication_positive(self):
        result = Calculator.multiply(4, 5)
        assert result == 20
    
    def test_multiplication_by_zero(self):
        result = Calculator.multiply(5, 0)
        assert result == 0
    
    def test_multiplication_negative(self):
        result = Calculator.multiply(-3, 4)
        assert result == -12
    
    def test_division_basic(self):
        result = Calculator.divide(15, 3)
        assert result == 5
    
    def test_division_decimal_result(self):
        result = Calculator.divide(7, 2)
        assert result == pytest.approx(3.5)
    
    def test_division_by_zero_raises_error(self):
        with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed"):
            Calculator.divide(10, 0)
