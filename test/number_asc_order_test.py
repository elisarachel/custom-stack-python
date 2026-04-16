import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_returns_numbers_in_ascending_order():
    # Pilha de 6 posições com 6 números sorteados da Mega Sena
    stack = CustomStack(6)
    drawn_numbers = [4, 23, 51, 7, 38, 15]
    for number in drawn_numbers:
        stack.push(number)

    cut = NumberAscOrder()
    result = cut.sort(stack)

    assert result == sorted(drawn_numbers)


def test_sort_empty_stack_returns_empty_list():
    # Pilha de 6 posições, vazia
    stack = CustomStack(6)

    cut = NumberAscOrder()
    result = cut.sort(stack)

    assert result == []
