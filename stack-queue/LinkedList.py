

class LinkedListNode(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, item):
        self.data = item

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):

    def __init__(self):
        self.head = None;

    def is_empty(self):
        print "No item in stack"
        return self.head is None

    # def is_full(self):
    #     return self.head==None

    def add(self, item):
        new_node = LinkedListNode(item)
        new_node.set_next(self.head)       #setting the next unknown node to null
        self.head = new_node

    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.get_next()
        print count

    def list_traverse(self):
        curr = self.head
        if self.head is None:
            return self.is_empty()
        else:
            while curr is not None:
                print curr.get_data()
                curr = curr.get_next()

    def remove_from_top(self):
        """
        :rtype:
        """
        curr = self.head
        if self.head is None:
            return self.is_empty()
        else:
            self.head = curr.get_next()
            curr = None


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add(10)
    linked_list.add(12)
    linked_list.add(13)
    linked_list.add(15)
    linked_list.size()
    linked_list.list_traverse()



