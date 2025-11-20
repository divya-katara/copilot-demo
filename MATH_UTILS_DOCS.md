# Math Utils Documentation

## Overview
This module provides various mathematical utility functions and a Calculator class with operation history tracking.

## Functions

### calculate_circle_area(radius)
Calculate the area of a circle.

**Parameters:**
- `radius` (float): The radius of the circle

**Returns:**
- float: The area of the circle

**Example:**
```python
>>> calculate_circle_area(5)
78.53975
```

### calculate_rectangle_area(length, width)
Calculate the area of a rectangle.

**Parameters:**
- `length` (float): The length of the rectangle
- `width` (float): The width of the rectangle

**Returns:**
- float: The area of the rectangle

### calculate_triangle_area(base, height)
Calculate the area of a triangle.

**Parameters:**
- `base` (float): The base of the triangle
- `height` (float): The height of the triangle

**Returns:**
- float: The area of the triangle

### Temperature Conversion Functions

#### convert_celsius_to_fahrenheit(celsius)
Convert temperature from Celsius to Fahrenheit.

#### convert_fahrenheit_to_celsius(fahrenheit)
Convert temperature from Fahrenheit to Celsius.

### is_prime(number)
Check if a number is prime.

**Parameters:**
- `number` (int): The number to check

**Returns:**
- bool: True if prime, False otherwise

### factorial(n)
Calculate the factorial of a number (n!).

### fibonacci(n)
Calculate the nth Fibonacci number.

## Calculator Class

A simple calculator with operation history tracking.

**Methods:**
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers (raises ValueError if dividing by zero)
- `get_history()` - Get calculation history

**Example Usage:**
```python
calc = Calculator()
calc.add(5, 3)  # Returns 8
calc.multiply(4, 2)  # Returns 8
print(calc.get_history())  # ['5 + 3 = 8', '4 * 2 = 8']
```

---

*Documentation generated with GitHub Copilot assistance*
