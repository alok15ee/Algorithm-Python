
from LinkedList import LinkedList, LinkedListNode


class Stack(object):

    def __init__(self):
        self.linked_list = LinkedList()

    def push(self, item):
        self.linked_list.add(item)

    def pop(self):
        self.linked_list.remove_from_top()

    def display_stack(self):
        self.linked_list.size()
        self.linked_list.list_traverse()

if __name__ == '__main__':

    stack = Stack()
    stack.push(61)
    stack.push(67)
    stack.push(57)

    stack.display_stack()
    stack.pop()
    stack.display_stack()
