# Copilot Demo Project

Welcome to the Copilot Demo Project documentation!

## Overview

This project demonstrates the integration of GitHub Copilot with automated testing and continuous integration workflows. It showcases various features including AI-assisted coding, refactoring, debugging, and documentation generation.

## Project Features

- ✅ Automated testing with pytest
- ✅ GitHub Actions CI/CD pipeline
- ✅ AI-assisted code generation and refactoring
- ✅ Comprehensive documentation
- ✅ Bug detection and correction examples

## API Overview

### Mathematical Utilities

Our `math_utils` module provides a comprehensive set of mathematical functions:

#### Area Calculations
- **Circle Area**: Calculate the area of a circle given its radius
- **Rectangle Area**: Calculate the area of a rectangle given length and width  
- **Triangle Area**: Calculate the area of a triangle given base and height

#### Temperature Conversions
- **Celsius to Fahrenheit**: Convert temperatures from Celsius to Fahrenheit
- **Fahrenheit to Celsius**: Convert temperatures from Fahrenheit to Celsius

#### Number Theory
- **Prime Number Check**: Determine if a number is prime
- **Factorial**: Calculate the factorial of a number
- **Fibonacci**: Generate Fibonacci sequence numbers

### Calculator Class

A feature-rich calculator that tracks operation history:

```python
from math_utils_with_docs import Calculator

calc = Calculator()
result = calc.add(10, 5)  # Returns 15
result = calc.multiply(3, 4)  # Returns 12
history = calc.get_history()  # View all operations
```

**Supported Operations:**
- Addition
- Subtraction
- Multiplication
- Division (with zero-division protection)

## Usage

### Installation

```bash
git clone https://github.com/divya-katara/copilot-demo.git
cd copilot-demo
pip install -r requirements.txt
```

### Running Tests

```bash
pytest test_app.py -v
pytest test_helpers.py -v
```

### Example Usage

```python
from app import add
from helpers import calculate_average

# Simple addition
result = add(5, 3)  # Returns 8

# Calculate average
numbers = [10, 20, 30, 40, 50]
avg = calculate_average(numbers)  # Returns 30.0
```

## GitHub Actions Workflow

This project includes automated testing that runs on every push:

- ✅ Python environment setup
- ✅ Dependency installation
- ✅ Automated test execution
- ✅ Test result reporting

View our [GitHub Actions workflows](https://github.com/divya-katara/copilot-demo/actions) for real-time CI/CD status.

## Code Quality Examples

### Refactoring Example

We demonstrate how GitHub Copilot helps refactor repetitive code into clean, maintainable classes:

**Before**: Repetitive student data processing  
**After**: Clean Student class with reusable methods

See [student_data_refactored.py](https://github.com/divya-katara/copilot-demo/blob/main/student_data_refactored.py)

### Bug Detection

Examples of identifying and fixing subtle bugs:

- **Sort Side Effects**: Demonstrating the difference between `sort()` and `sorted()`
- **Logical Errors**: Fixing division by zero in average calculations

## Documentation

- [Math Utils Documentation](MATH_UTILS_DOCS.md)
- [Test Coverage](test_app.py)
- [GitHub Repository](https://github.com/divya-katara/copilot-demo)

## AI-Assisted Development

This project leverages GitHub Copilot for:

- 🤖 Code generation and suggestions
- 📝 Automatic docstring generation
- 🔍 Bug detection and fixes
- ♻️ Code refactoring recommendations
- ✅ Test case generation

**Benefits of AI-Assisted Documentation:**

1. **Consistency**: All functions follow the same documentation format
2. **Completeness**: Every parameter and return value is documented
3. **Time Savings**: Reduces manual documentation effort by ~70%
4. **Code Examples**: Automatic generation of usage examples

## Contributing

Contributions are welcome! Please ensure all tests pass before submitting a pull request.

## License

MIT License

---

*This documentation was created with assistance from GitHub Copilot*  
*Last updated: November 20, 2025*
