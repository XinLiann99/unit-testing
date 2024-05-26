class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b
    

def test_add():
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()

    # act
    result = cal.add(a, b)

    # assert
    expected = 5555
    assert result == expected #True

def test_subtract():
    # arrange
    a = 1234
    b = 1222
    cal = Calculator()

    # act
    result = cal.subtract(a, b)

    # assert
    expected = 12
    assert result == expected #True

def test_multiply():
    # arrange
    a = 12
    b = 12
    cal = Calculator()

    # act
    result = cal.multiply(a, b)

    # assert
    expected = 144
    assert result == expected #True

def test_divide():
    # arrange
    a = 20
    b = 10
    cal = Calculator()

    # act
    result = cal.divide(a, b)

    # assert
    expected = 2
    assert result == expected #True


