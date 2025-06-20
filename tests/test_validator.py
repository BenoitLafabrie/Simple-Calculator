import pytest
from src.validator import NumberValidator

class TestNumberValidator:
    
    @pytest.mark.parametrize("input_str,expected", [
        ("123", True),
        ("123.45", True),
        ("-123", True),
        ("-123.45", True),
        ("0.123", True),
        (".123", True),
        ("0", True),
        ("", False),
        ("   ", False),
        ("abc", False),
        ("12a3", False),
        ("12.34.56", False),
    ])
    def test_is_number_validation(self, input_str, expected):
        assert NumberValidator.is_number(input_str) == expected
    
    def test_cast_valid_integer(self):
        result = NumberValidator.cast_number("123")
        assert result == 123
        assert isinstance(result, int)
    
    def test_cast_valid_float(self):
        result = NumberValidator.cast_number("123.45")
        assert result == 123.45
        assert isinstance(result, float)
    
    def test_cast_negative_number(self):
        result = NumberValidator.cast_number("-42")
        assert result == -42
    
    def test_cast_invalid_string_raises_error(self):
        with pytest.raises(ValueError, match="'abc' is not a valid number"):
            NumberValidator.cast_number("abc")
