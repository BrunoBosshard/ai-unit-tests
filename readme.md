# Automatically generated Artificial Intelligence (AI) Unit Tests with documentation for existing program code

This example shows the power of automatically generated Artificial Intelligence (AI) Unit Tests for existing program code. Note that it also generates documentation and meaningful additional Unit Tests, such as `test_divide_by_zero`.

This project works with the Google [Gemini Pro](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/models) Large Language Model (LLM).

You need a Google Generative AI API key for this project. [Get your free API key here](https://makersuite.google.com/app/apikey). Insert your Google API key in the "ai-unit-tests.py" file.

**Unit Tests are automatically created for this Python program code:**

```
class Calculator:
    def add(self, left, right):
        return left + right

    def subtract(self, left, right):
        return left - right

    def multiply(self, left, right):
        return left * right

    def divide(self, left, right):
        return left / right
```

**These are the automatically generated Unit Tests, including documentation:**

```python
import unittest

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        calculator = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
```

These test cases are designed to achieve the following:

1. `test_add`: This test case checks if the `add` method of the `Calculator` class correctly adds two numbers. It asserts that the result of adding 1 and 2 is 3.

2. `test_subtract`: This test case checks if the `subtract` method of the `Calculator` class correctly subtracts two numbers. It asserts that the result of subtracting 3 from 5 is 2.

3. `test_multiply`: This test case checks if the `multiply` method of the `Calculator` class correctly multiplies two numbers. It asserts that the result of multiplying 4 and 5 is 20.

4. `test_divide`: This test case checks if the `divide` method of the `Calculator` class correctly divides two numbers. It asserts that the result of dividing 10 by 2 is 5.

5. `test_divide_by_zero`: This test case checks if the `divide` method of the `Calculator` class raises a `ZeroDivisionError` when dividing by zero. It uses the `with self.assertRaises(ZeroDivisionError)` context manager to assert that a `ZeroDivisionError` is raised when dividing 1 by 0.
