def process_numbers(numbers):
    """Process a list of numbers and return some result."""
    # Use Copilot to suggest helpful helper functions
    def filter_even_numbers(nums):
        """Filter out even numbers from the list."""
        return [num for num in nums if num % 2 != 0]

# Function with logical error - calculate average
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total = total + num
    # Fixed: Properly divide by the length of the list
    return total / len(numbers)    
    