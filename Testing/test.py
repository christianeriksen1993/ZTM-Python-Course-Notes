import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdefh'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = [5, 4]
        result = main.do_stuff(test_param)
        self.assertListEqual(result, [10, 9])

    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")


    def test_guess_true(self):
        result = main.guess_func(5, 5)
        self.assertTrue(result)

    def test_guess_wrong(self):
        result = main.guess_func(5, 0)
        self.assertFalse(result)
    
    def test_guess_OutOfRange(self):
        result = main.guess_func(5, 31)
        self.assertFalse(result)

    def test_guess_string(self):
        result = main.guess_func(5, '5')
        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()