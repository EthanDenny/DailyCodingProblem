import collections
from enum import Enum


class BracketStyle(Enum):
    ROUND = 0
    CURLY = 1
    SQUARE = 2


def f(string):
    stack = collections.deque()

    for c in string:
        if c == '(':
            stack.append(BracketStyle.ROUND)
        elif c == '{':
            stack.append(BracketStyle.CURLY)
        elif c == '[':
            stack.append(BracketStyle.SQUARE)
        elif c == ')':
            if stack.pop() != BracketStyle.ROUND: return False
        elif c == '}':
            if stack.pop() != BracketStyle.CURLY: return False
        elif c == ']':
            if stack.pop() != BracketStyle.SQUARE: return False

    return len(stack) == 0


if __name__ == '__main__':
    assert f('([])[]({})') == True
    assert f('([)]') == False
    assert f('((()') == False
