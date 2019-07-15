from LinkedList import LinkedList;
from Node import Node;

# Implement as subclass of LinkedList
class Stack:
    #def __init__(self, value = None):
     #   LinkedList.__init__(self, value);
      #  self.top = self.get_head_node();
    def __init__(self, limit = 1000):
        self.top_item = None;
        self.size = 0;
        self.limit = limit;

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value();
        else:
            print('The stack is empty');

    def push(self, value):
        if self.has_space():
            item = Node(value);
            item.set_next_node(self.top_item);
            self.top_item = item;
            self.size += 1;
        else:
            print('Stack is full, cannot push {}'.format(value));

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item;
            self.top_item = item_to_remove.get_next_node();
            self.size -= 1;
            return item_to_remove.get_value();
        else:
            print('The stack is empty, cannot pop.');

    def has_space(self):
        return self.size < self.limit;

    def is_empty(self):
        return self.size == 0;