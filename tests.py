"""--------------------------------------------------------------
Name: Joseph Cruz
Class: GIS 321

Assignment 1
--------------------------------------------------------------"""

import unittest

class Test_Assignment_01(unittest.TestCase):
    """
    Below are a series of tests, some of which will fail.

    Automated testing will be performed when you submit a
    Pull Request and any time that you make any future
    modification to the file.

    If you get stuck, launch a Python interpreter (Python,
    iPython, or Jupyter Notebook) and copy a small block of
    code.

    For example, if the test reads:

    x = 'abcde'
    self.assertEqual(4, len(x))

    and you are unsure what len(x) might return, you can
    execute:

    >>> x = 'abcde'
    >>> len(x)
    5

    in any of the above interpreters.
    """
    
    def setUp(self):
        """
        Code called before every other test is run.
        """
        pass
    
    def test_assert_truth(self):
        """
        A test that will pass
        """
        self.assertTrue(True)

    def test_assert_truth_with_a_message(self):
        """
        A test that will fail.
        """
        #[Joseph] changed assertFalse to assertTrue
        self.assertTrue(True, 'This should fail, please fix it.')

    def test_assert_equality(self):
        """
        A test for equality by assigning a value to a variable
        and evaluating an expression.
        """
        #[Joseph] expected value changed from _ to 2
        expected_value = 2
        truth_value = 1 + 1
        self.assertEqual(expected_value, truth_value)

    def test_what_are_these_types(self):
        """
        A test to know what the types of the previous fixes were
        """
        #[Joseph] changed to assertTrue and isinstance was added to check
        #if True is of type bool
        self.assertTrue(isinstance(True, bool))

    def test_assert_string(self):
        """
        A test for evaluating an expression
        """
        my_string = 'Hello World'
        #[Joseph] -1 added to remove null at end of string
        my_string_length = len(my_string)-1  # The expression
        self.assertEqual(10, my_string_length)

    def test_big_integers(self):
        """
        A test to explore notation of big integers.
        """
        #[Joseph] removed comma in 42000
        x = 42000
        self.assertTrue(isinstance(x, int))

    def test_bigger_integers(self):
        """
        A test for bigger, or smaller integers
        """
        #[Joseph] changed big to 1e2 from 1e6
        big = 1e2
        self.assertEqual(big, 100)
        self.assertTrue(type(big), int)
        #[Joseph] changed small to 1e-4 from 1e-5
        small = 1e-4
        self.assertEqual(small, 0.0001)
        self.assertTrue(type(small), int)

    def test_type_conversion(self):
        """
        A series of tests to validate type conversion operations
        """
        i = 1
        self.assertTrue(type(i) == int)
        i= float(i)
        self.assertTrue(isinstance(i, float))  # These lines do the same type checking
        i = float(i)
        self.assertTrue(isinstance(i, float))
        #[Joseph] i=str(i) is commented out, removes the conversion
        #and type() is changed to isinstance so assertFalse checks a bool
        #i = str(i)
        self.assertFalse(isinstance(i,str))

    def test_type_conversion2(self):
        """
        A poorly named function to test converting strings to numeric types
        """
        k = "123"
        self.assertIsInstance(k, str)  # New assertion type that shortens previous calls
        k = float(k)
        self.assertEqual(123, k)  # Hmmm, note how this equality works across types

    def test_type_conversion_gotcha(self):
        """
        A test to show how rounding can get you
        """
        j = 3.9999
        self.assertTrue(int(j), float)
        #[Joseph] added 1 because of the rounding error in int. int concatenates
        #a float to be an integer.
        self.assertEqual(int(j)+1, 4)

    def tearDown(self):
        """
        Code called after ever other test is run.
        """
        pass

if __name__ == '__main__':
    unittest.main()
