import unittest

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado


class TestFibonacci(unittest.TestCase):
    def test_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado,0)

    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado,1)

    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado,1)

    def test_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado,5)

    def test_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado,8)

    def test_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado,13)

    def test_10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado,55)

unittest.main()



