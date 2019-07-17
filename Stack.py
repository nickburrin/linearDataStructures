from LinkedList import LinkedList;
from Node import Node;

# Implement as subclass of LinkedList
class Stack(LinkedList):
    def __init__(self, limit = 1000):
        LinkedList.__init__(self, None);
        self.top_item = self.get_head_node();
        self.size = 0;
        self.limit = limit;

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value();
        else:
            print('The stack is empty');

    def push(self, value):
        if self.has_space():
            self.insert_beginning(value);
            self.top_item = self.get_head_node()
            self.size += 1;
        else:
            print('Stack is full, cannot push {}'.format(value));

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.remove_head();
            self.top_item = self.get_head_node()
            self.size -= 1;
            return item_to_remove.get_value();
        else:
            print('The stack is empty, cannot pop.');

    def has_space(self):
        return self.size < self.limit;

    def is_empty(self):
        return self.size == 0;