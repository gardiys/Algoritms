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
        self.last = self.last.link

l = OneLinkedList()
l.add(1)
l.add(2)
l.add(5)
l.add(3)
l.add(4)


#l.pop()

print(*l.get_items())