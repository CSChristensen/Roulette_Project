#!/usr/bin/env python3
"""
Unit tests for number input validation in the GameController.
Tests validate_number_choice method with various inputs including edge cases.
"""

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False

from src.game_controller import GameController
from src.bet import BetType


class TestNumberValidation:
    """Test class for number input validation methods."""

    def setup_method(self):
        """Setup method to provide a GameController instance for tests."""
        self.controller = GameController()

    def test_validate_number_choice_valid_inputs(self):
        """Test validate_number_choice with all valid inputs (0-36)."""
        # Test all valid numbers from 0 to 36
        for number in range(37):  # 0 to 36 inclusive
            result = self.controller.validate_number_choice(str(number))
            assert result == number, f"Number {number} should be valid"

    def test_validate_number_choice_boundary_values(self):
        """Test boundary values for number validation."""
        # Test minimum boundary (0)
        result = self.controller.validate_number_choice("0")
        assert result == 0, "Zero should be valid"

        # Test maximum boundary (36)
        result = self.controller.validate_number_choice("36")
        assert result == 36, "Thirty-six should be valid"

    def test_validate_number_choice_invalid_negative(self):
        """Test validation with negative numbers."""
        invalid_negatives = ["-1", "-5", "-10", "-100"]
        
        for negative in invalid_negatives:
            result = self.controller.validate_number_choice(negative)
            assert result is None, f"Negative number {negative} should be invalid"

    def test_validate_number_choice_invalid_too_large(self):
        """Test validation with numbers greater than 36."""
        invalid_large = ["37", "38", "50", "100", "999"]
        
        for large in invalid_large:
            result = self.controller.validate_number_choice(large)
            assert result is None, f"Number {large} should be invalid (too large)"

    def test_validate_number_choice_non_numeric(self):
        """Test validation with non-numeric inputs."""
        non_numeric_inputs = [
            "abc", "red", "black", "green", "hello", "xyz",
            "1a", "a1", "12b", "b12", "1.5a", "a1.5"
        ]
        
        for non_numeric in non_numeric_inputs:
            result = self.controller.validate_number_choice(non_numeric)
            assert result is None, f"Non-numeric input '{non_numeric}' should be invalid"

    def test_validate_number_choice_decimal_numbers(self):
        """Test validation with decimal numbers."""
        decimal_inputs = ["1.5", "10.0", "25.7", "0.5", "36.1", "12.34"]
        
        for decimal in decimal_inputs:
            result = self.controller.validate_number_choice(decimal)
            assert result is None, f"Decimal number '{decimal}' should be invalid"

    def test_validate_number_choice_empty_input(self):
        """Test validation with empty inputs."""
        empty_inputs = ["", "   ", "\t", "\n", "  \t  \n  "]
        
        for empty in empty_inputs:
            result = self.controller.validate_number_choice(empty)
            assert result is None, f"Empty input '{repr(empty)}' should be invalid"

    def test_validate_number_choice_whitespace_handling(self):
        """Test that validation handles whitespace correctly."""
        whitespace_cases = [
            ("  5  ", 5),
            (" 0 ", 0),
            ("36   ", 36),
            ("   12", 12),
            ("\t25\t", 25),
            (" \n 18 \n ", 18)
        ]
        
        for input_str, expected in whitespace_cases:
            result = self.controller.validate_number_choice(input_str)
            assert result == expected, f"Input '{repr(input_str)}' should return {expected}"

    def test_validate_number_choice_special_characters(self):
        """Test validation with special characters."""
        special_char_inputs = [
            "5!", "@12", "#25", "$30", "%15", "^20", "&8", "*11",
            "5+", "12-", "18=", "25_", "30|", "5\\", "12/", "18?"
        ]
        
        for special in special_char_inputs:
            result = self.controller.validate_number_choice(special)
            assert result is None, f"Input with special characters '{special}' should be invalid"

    def test_validate_number_choice_comma_separated(self):
        """Test validation with comma-separated numbers."""
        comma_inputs = ["1,000", "5,5", "12,34", "1,2,3"]
        
        for comma_input in comma_inputs:
            result = self.controller.validate_number_choice(comma_input)
            assert result is None, f"Comma-separated input '{comma_input}' should be invalid"

    def test_validate_number_choice_scientific_notation(self):
        """Test validation with scientific notation."""
        scientific_inputs = ["1e2", "5E1", "2.5e1", "1.0E+1"]
        
        for scientific in scientific_inputs:
            result = self.controller.validate_number_choice(scientific)
            assert result is None, f"Scientific notation '{scientific}' should be invalid"

    def test_validate_number_choice_hexadecimal(self):
        """Test validation with hexadecimal numbers."""
        hex_inputs = ["0x10", "0X20", "0xff", "0xFF", "A", "F", "1A"]
        
        for hex_input in hex_inputs:
            result = self.controller.validate_number_choice(hex_input)
            assert result is None, f"Hexadecimal input '{hex_input}' should be invalid"

    def test_validate_number_choice_binary_octal(self):
        """Test validation with binary and octal numbers."""
        binary_octal_inputs = ["0b101", "0B111", "0o17", "0O20", "101b", "17o"]
        
        for binary_octal in binary_octal_inputs:
            result = self.controller.validate_number_choice(binary_octal)
            assert result is None, f"Binary/octal input '{binary_octal}' should be invalid"

    def test_validate_number_choice_unicode_numbers(self):
        """Test validation with unicode number characters."""
        unicode_inputs = ["①", "②", "⑤", "⑩", "½", "¼", "²", "³"]
        
        for unicode_num in unicode_inputs:
            result = self.controller.validate_number_choice(unicode_num)
            assert result is None, f"Unicode number '{unicode_num}' should be invalid"

    def test_validate_number_choice_very_long_strings(self):
        """Test validation with very long strings."""
        long_inputs = [
            "1" * 100,  # Very long number
            "a" * 50,   # Very long non-numeric
            "12345678901234567890",  # Very large number
        ]
        
        for long_input in long_inputs:
            result = self.controller.validate_number_choice(long_input)
            assert result is None, f"Very long input should be invalid"

    def test_validate_number_choice_mixed_valid_invalid(self):
        """Test a comprehensive mix of valid and invalid inputs."""
        test_cases = [
            # (input, expected_result, description)
            ("0", 0, "minimum valid"),
            ("36", 36, "maximum valid"),
            ("18", 18, "middle valid"),
            ("-1", None, "just below minimum"),
            ("37", None, "just above maximum"),
            ("", None, "empty string"),
            ("  ", None, "whitespace only"),
            ("5.0", None, "decimal zero"),
            ("05", 5, "leading zero"),
            ("  15  ", 15, "whitespace padded"),
            ("abc", None, "letters only"),
            ("12abc", None, "number with letters"),
            ("abc12", None, "letters with number"),
            ("1 2", None, "space in middle"),
            ("1-2", None, "dash in middle"),
            ("1+2", None, "plus in middle"),
        ]
        
        for input_str, expected, description in test_cases:
            result = self.controller.validate_number_choice(input_str)
            assert result == expected, f"Failed for {description}: input='{input_str}', expected={expected}, got={result}"

    def test_get_bet_type_number_selection(self):
        """Test that get_bet_type correctly handles number betting selection."""
        # This is an integration test to ensure number betting is properly supported
        # We can't easily test the interactive input, but we can test the validation logic
        
        # Test that BetType.NUMBER is a valid enum value
        assert BetType.NUMBER.value == "number"
        
        # Test that the controller has the validate_number_choice method
        assert hasattr(self.controller, 'validate_number_choice')
        assert callable(getattr(self.controller, 'validate_number_choice'))

    def test_error_message_accuracy(self):
        """Test that error messages are helpful and accurate."""
        # We can't easily capture the display_message output in unit tests,
        # but we can verify that invalid inputs return None consistently
        
        error_cases = [
            "-1",      # Below range
            "37",      # Above range  
            "abc",     # Non-numeric
            "",        # Empty
            "5.5",     # Decimal
            "1,000",   # Comma
        ]
        
        for error_case in error_cases:
            result = self.controller.validate_number_choice(error_case)
            assert result is None, f"Error case '{error_case}' should return None"

    def test_validate_number_choice_stress_test(self):
        """Stress test with many different inputs to ensure robustness."""
        # Test all valid numbers multiple times
        for _ in range(3):  # Run multiple iterations
            for num in range(37):
                result = self.controller.validate_number_choice(str(num))
                assert result == num, f"Stress test failed for number {num}"
        
        # Test many invalid cases
        invalid_cases = []
        for i in range(-10, 0):  # Negative numbers
            invalid_cases.append(str(i))
        for i in range(37, 50):  # Too large numbers
            invalid_cases.append(str(i))
        
        for invalid in invalid_cases:
            result = self.controller.validate_number_choice(invalid)
            assert result is None, f"Stress test failed for invalid input {invalid}"


def run_standalone_tests():
    """Run tests without pytest for environments where it's not available."""
    print("Running number validation tests...")

    test_instance = TestNumberValidation()
    test_methods = [
        "test_validate_number_choice_valid_inputs",
        "test_validate_number_choice_boundary_values",
        "test_validate_number_choice_invalid_negative",
        "test_validate_number_choice_invalid_too_large",
        "test_validate_number_choice_non_numeric",
        "test_validate_number_choice_decimal_numbers",
        "test_validate_number_choice_empty_input",
        "test_validate_number_choice_whitespace_handling",
        "test_validate_number_choice_special_characters",
        "test_validate_number_choice_comma_separated",
        "test_validate_number_choice_scientific_notation",
        "test_validate_number_choice_hexadecimal",
        "test_validate_number_choice_binary_octal",
        "test_validate_number_choice_unicode_numbers",
        "test_validate_number_choice_very_long_strings",
        "test_validate_number_choice_mixed_valid_invalid",
        "test_get_bet_type_number_selection",
        "test_error_message_accuracy",
        "test_validate_number_choice_stress_test",
    ]

    passed = 0
    failed = 0

    for method_name in test_methods:
        try:
            test_instance.setup_method()
            method = getattr(test_instance, method_name)
            method()
            print(f"✓ {method_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {method_name}: {e}")
            failed += 1

    print(f"\nTest Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    if PYTEST_AVAILABLE:
        pytest.main([__file__, "-v"])
    else:
        success = run_standalone_tests()
        exit(0 if success else 1)