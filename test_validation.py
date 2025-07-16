#!/usr/bin/env python3
"""
Test suite to verify the enhanced validation methods work correctly.
Can be run with pytest (if available) or as a standalone script.
"""

try:
    import pytest

    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False

from game_controller import GameController
from wheel import Color


class TestGameControllerValidation:
    """Test class for GameController validation methods."""

    def setup_method(self):
        """Setup method to provide a GameController instance for tests."""
        self.controller = GameController()

    def test_validate_positive_integer(self):
        """Test positive integer validation with various inputs."""
        test_cases = [
            ("100", True, 100),
            ("1", True, 1),
            ("1000000", True, 1000000),
            ("0", False, None),
            ("-5", False, None),
            ("abc", False, None),
            ("", False, None),
            ("  ", False, None),
            ("10.5", False, None),
            ("1,000", False, None),
            ("2000000", False, None),  # Too large
        ]

        for test_input, expected_valid, expected_value in test_cases:
            result = self.controller.validate_positive_integer(test_input, "test")
            is_valid = result is not None

            assert is_valid == expected_valid, f"Input '{test_input}' validation failed"
            if expected_valid:
                assert result == expected_value, (
                    f"Expected {expected_value}, got {result}"
                )

    def test_validate_color_choice(self):
        """Test color choice validation with various inputs."""
        test_cases = [
            ("red", Color.RED),
            ("RED", Color.RED),
            ("r", Color.RED),
            ("black", Color.BLACK),
            ("BLACK", Color.BLACK),
            ("b", Color.BLACK),
            ("green", Color.GREEN),
            ("GREEN", Color.GREEN),
            ("g", Color.GREEN),
            ("0", Color.GREEN),
            ("blue", None),
            ("", None),
            ("  ", None),
            ("yellow", None),
        ]

        for test_input, expected_color in test_cases:
            result = self.controller.validate_color_choice(test_input)
            assert result == expected_color, (
                f"Input '{test_input}' should return {expected_color}, got {result}"
            )

    def test_validate_yes_no(self):
        """Test yes/no validation with various inputs."""
        test_cases = [
            ("y", True),
            ("yes", True),
            ("YES", True),
            ("yeah", True),
            ("yep", True),
            ("1", True),
            ("true", True),
            ("n", False),
            ("no", False),
            ("NO", False),
            ("nope", False),
            ("0", False),
            ("false", False),
            ("maybe", None),
            ("", None),
            ("  ", None),
            ("invalid", None),
        ]

        for test_input, expected_bool in test_cases:
            result = self.controller.validate_yes_no(test_input)
            assert result == expected_bool, (
                f"Input '{test_input}' should return {expected_bool}, got {result}"
            )

    def test_validate_positive_integer_edge_cases(self):
        """Test edge cases for positive integer validation."""
        # Test maximum allowed value
        result = self.controller.validate_positive_integer("1000000", "test")
        assert result == 1000000

        # Test value just over maximum
        result = self.controller.validate_positive_integer("1000001", "test")
        assert result is None

        # Test whitespace handling
        result = self.controller.validate_positive_integer("  100  ", "test")
        assert result == 100

    def test_validate_color_choice_case_insensitive(self):
        """Test that color validation is truly case-insensitive."""
        test_cases = [
            ("Red", Color.RED),
            ("rEd", Color.RED),
            ("BLACK", Color.BLACK),
            ("Black", Color.BLACK),
            ("GREEN", Color.GREEN),
            ("Green", Color.GREEN),
        ]

        for test_input, expected in test_cases:
            result = self.controller.validate_color_choice(test_input)
            assert result == expected, (
                f"Case-insensitive test failed for '{test_input}'"
            )

    def test_validate_yes_no_comprehensive(self):
        """Test comprehensive yes/no validation including edge cases."""
        # Test all yes variations
        yes_inputs = [
            "y",
            "Y",
            "yes",
            "YES",
            "Yes",
            "yeah",
            "YEAH",
            "yep",
            "YEP",
            "1",
            "true",
            "TRUE",
        ]
        for yes_input in yes_inputs:
            result = self.controller.validate_yes_no(yes_input)
            assert result is True, f"'{yes_input}' should be recognized as True"

        # Test all no variations
        no_inputs = ["n", "N", "no", "NO", "No", "nope", "NOPE", "0", "false", "FALSE"]
        for no_input in no_inputs:
            result = self.controller.validate_yes_no(no_input)
            assert result is False, f"'{no_input}' should be recognized as False"


def run_standalone_tests():
    """Run tests without pytest for environments where it's not available."""
    print("Running validation tests...")

    test_instance = TestGameControllerValidation()
    test_methods = [
        "test_validate_positive_integer",
        "test_validate_color_choice",
        "test_validate_yes_no",
        "test_validate_positive_integer_edge_cases",
        "test_validate_color_choice_case_insensitive",
        "test_validate_yes_no_comprehensive",
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
