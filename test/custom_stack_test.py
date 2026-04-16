import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_one_element_in_stack():
    element_value = 5.0
    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_is_empty_when_new_stack():
    cut = CustomStack(3)
    assert cut.is_empty() == True


def test_size_is_zero_when_new_stack():
    cut = CustomStack(3)
    assert cut.size() == 0


def test_push_increases_size():
    cut = CustomStack(3)
    cut.push(10)
    cut.push(20)
    assert cut.size() == 2


def test_push_raises_stack_full_exception_when_at_limit():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    with pytest.raises(StackFullException):
        cut.push(3)


def test_pop_returns_last_pushed_element():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    assert cut.pop() == 2


def test_pop_decreases_size():
    cut = CustomStack(3)
    cut.push(1)
    cut.pop()
    assert cut.size() == 0


def test_pop_raises_stack_empty_exception_when_empty():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_raises_stack_empty_exception_when_empty():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.top()


def test_top_does_not_remove_element():
    cut = CustomStack(3)
    cut.push(42)
    assert cut.top() == 42
    assert cut.size() == 1
