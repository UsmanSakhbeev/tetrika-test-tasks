import pytest

from ..solution import strict


@strict
def add(a: int, b: int) -> int:
    return a + b


@strict
def mul_float(x: float, y: float) -> float:
    return x * y


@strict
def say(text: str) -> str:
    return text.upper()


@strict
def logical_and(p: bool, q: bool) -> bool:
    return p and q


def test_int_ok():
    assert add(2, 3) == 5


def test_float_ok():
    assert mul_float(1.5, 2.0) == 3.0


def test_str_ok():
    assert say("hey") == "HEY"


def test_bool_ok_kwargs():

    assert logical_and(p=True, q=False) is False


def test_int_receives_bool():
    with pytest.raises(TypeError):
        add(True, 1)


def test_float_receives_int():
    with pytest.raises(TypeError):
        mul_float(1, 2.0)


def test_str_receives_float():
    with pytest.raises(TypeError):
        say(3.14)
