"""
Mathematical utility functions with comprehensive docstrings.
This module provides various mathematical calculations and a Calculator class.
"""

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
        
    Example:
        >>> calculate_circle_area(5)
        78.53975
    """
    return 3.14159 * radius ** 2

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
    Returns:
        float: The area of the rectangle.
        
    Example:
        >>> calculate_rectangle_area(4, 5)
        20
    """
    return length * width

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.
    
    Args:
        base (float): The base of the triangle.
        height (float): The height of the triangle.
        
    Returns:
        float: The area of the triangle.
        
    Example:
        >>> calculate_triangle_area(10, 5)
        25.0
    """
    return 0.5 * base * height

def convert_celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius.
        
    Returns:
        float: Temperature in Fahrenheit.
        
    Example:
        >>> convert_celsius_to_fahrenheit(0)
        32.0
        >>> convert_celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit.
        
    Returns:
        float: Temperature in Celsius.
        
    Example:
        >>> convert_fahrenheit_to_celsius(32)
        0.0
        >>> convert_fahrenheit_to_celsius(212)
        100.0
    """
    return (fahrenheit - 32) * 5/9

def is_prime(number):
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    
    Args:
        number (int): The number to check.
        
    Returns:
        bool: True if the number is prime, False otherwise.
        
    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(n):
    """
    Calculate the factorial of a number.
    
    The factorial of n (denoted as n!) is the product of all positive 
    integers less than or equal to n.
    
    Args:
        n (int): A non-negative integer.
        
    Returns:
        int: The factorial of n.
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is the sum of the two preceding ones.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).
        
    Returns:
        int: The nth Fibonacci number.
        
    Example:
        >>> fibonacci(6)
        8
        >>> fibonacci(10)
        55
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class Calculator:
    """
    A simple calculator class with operation history tracking.
    
    This class provides basic arithmetic operations (add, subtract, multiply, divide)
    and maintains a history of all calculations performed.
    
    Attributes:
        history (list): A list of strings representing calculation history.
        
    Example:
        >>> calc = Calculator()
        >>> calc.add(5, 3)
        8
        >>> calc.multiply(4, 2)
        8
        >>> calc.get_history()
        ['5 + 3 = 8', '4 * 2 = 8']
    """
    
    def __init__(self):
        """Initialize a new Calculator with an empty history."""
        self.history = []
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): The first number.
            b (float): The second number.
            
        Returns:
            float: The sum of a and b.
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """
        Subtract the second number from the first.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
            
        Returns:
            float: The difference of a and b.
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float): The first number.
            b (float): The second number.
            
        Returns:
            float: The product of a and b.
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """
        Divide the first number by the second.
        
        Args:
            a (float): The dividend.
            b (float): The divisor.
            
        Returns:
            float: The quotient of a and b.
            
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """
        Get the calculation history.
        
        Returns:
            list: A list of strings representing all calculations performed.
        """
        return self.history
