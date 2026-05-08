import pytest
from fib_generator import generate_fibonacci


class TestGenerateFibonacci:
    """Tests for the generate_fibonacci function."""

    def test_negative_limit_raises_valueerror(self):
        """Test that negative limits raise ValueError."""
        with pytest.raises(ValueError, match="Limit must be non-negative"):
            generate_fibonacci(-1)
        
        with pytest.raises(ValueError):
            generate_fibonacci(-10)

    def test_limit_zero_returns_empty_list(self):
        """Test that limit=0 returns an empty list."""
        result = generate_fibonacci(0)
        assert result == []

    def test_limit_one_returns_first_two_fibonacci(self):
        """Test that limit=1 returns [0, 1, 1] (the third 1 exceeds the limit)."""
        result = generate_fibonacci(1)
        assert result == [0, 1, 1]

    def test_small_limit(self):
        """Test with a small limit value."""
        result = generate_fibonacci(10)
        assert result == [0, 1, 1, 2, 3, 5, 8]

    def test_limit_is_fibonacci_number(self):
        """Test when limit is exactly a Fibonacci number."""
        result = generate_fibonacci(8)
        assert result == [0, 1, 1, 2, 3, 5, 8]

    def test_larger_limit(self):
        """Test with a larger limit value."""
        result = generate_fibonacci(100)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        assert result == expected

    def test_large_limit(self):
        """Test with a large limit value."""
        result = generate_fibonacci(10000)
        assert result[-1] <= 10000
        assert len(result) > 20

    def test_specific_fibonacci_values(self):
        """Verify that specific Fibonacci numbers are generated correctly."""
        result = generate_fibonacci(1000)
        
        known_fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
        for fib in known_fibs:
            assert fib in result
        
        assert result.index(987) == 16
        assert 1597 not in result

    def test_sequence_order(self):
        """Test that the sequence is in ascending order."""
        result = generate_fibonacci(1000)
        assert result == sorted(result)

    def test_sequence_increases(self):
        """Test that sequence increases (except for the 1,1 duplicate)."""
        result = generate_fibonacci(100)
        
        for i in range(1, len(result)):
            if result[i] != result[i-1]:
                assert result[i] > result[i-1]
