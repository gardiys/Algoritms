class Node:

    def __init__(self, value, link=None):
        self.value = value
        self.link = link


class OneLinkedList:

    def __init__(self):
        self.last = None

    def add(self, value):

        node = Node(value, self.last)
        self.last = node

    def get_items(self):
        last = self.last
        while last is not None:
            yield last.value
            last = last.link

    def pop(self):
        last = self.last
        self.last = self.last.link
        return last


class Stack:

    def __init__(self):
        self.data = OneLinkedList()

    def append(self, value):
        self.data.add(value)

    def pop(self):
        return self.data.pop().value

    def peek(self):
        return self.data.last.value

from collections import deque

class NormalStack:

    def __init__(self):
        self.data = deque()

    def append(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()


    def peek(self):
        elem = self.data.pop()
        self.data.append(elem)
        return elem
