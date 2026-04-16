from src.custom_stack_class import CustomStack, StackEmptyException


class NumberAscOrder:

    def sort(self, stack: CustomStack) -> list:
        if stack.is_empty():
            return []

        result = []
        while not stack.is_empty():
            result.append(stack.pop())

        return sorted(result)
