from helpers import calculate_average

def test_calculate_average():
    """Test the calculate_average function."""
    # This will fail due to the logical error
    result = calculate_average([10, 20, 30, 40])
    assert result == 25.0
