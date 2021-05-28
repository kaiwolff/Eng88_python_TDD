# Test Drive Development
# Pytest and Unittest
#### Use pip to install the packages

TDD stands for Test-Driven Development.

The idea is that nothing is sent to production before it is tested. Using a car as an example, a tire for the car may be made separately. If the main manufacturer sends specifications such as the top speed the tire would need to be able to withstand for some amount of time. The same might happen with the brakes. This would happen for all components in the car. 

Similarly, in TDD, we write tests for our software first, then focus on passing those tests with our code to ensure we deliver what the product owner has asked for.

### TDD

- Starts with RED everything failing before writing functional code to pass tests
- GREEN write or refactor the code to pass test
- BLUE Refactoring - start again with next tests

`unittest` and `pytest`

### Exercise

- Create a file to write our tests - for a calculator class.
- then create a file to add functionality to pass the tests with a basic calculator.

#### Naming convention'

"test" is an important keyword and is necessary for pytest to recognise functions designed to test 


### Writing Tests 

```python
import pytest
import unittest

from SimpleCalc import SimpleCalc

class CalcTest(unittest.TestCase):
    #inheriting TestCase class from unittest

    calc = SimpleCalc()

    def test_add(self): # naming convention is essential as 'test' is the word that we need to use when naming tests so python interpreter recognises it as a testcase.
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 4), 0.5)
```

### Commands for running tests:

`python -m unittest discover -v` and 

`python -m unittest`. The discover option gives more information. 
### Test-Driven Development

Running this file's tests will attempt to run the corresponding, and return information on the success or failure of these functions. 

Having written the tests for the software, we can now write code to satisfy our test cases. In this case, I used the calculator programmed as part of the object-oriented programming exercise to attempt to satisfy the tests. Once the tests are passed, we refactor our code, and design further tests if necessary.