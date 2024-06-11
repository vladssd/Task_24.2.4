import pytest

from api.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc  = Calculator

    def test_adding_sucsess(self):
        assert self.calc.adding(self, 1,1) ==  2

    def test_substract(self):   # метод вычитания
        assert self.calc.subtraction(self,5, 4) == 1

    def test_multiply(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_adding_unsucsess(self):
        assert self.calc.adding(self, 1,1) == 3

    def test_division(self):
        assert self.calc.division(self, 12, 2) == 6

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')