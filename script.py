class Node:
    def __init__(self, value, next_node = None):
        self.value = value;
        self.next_node = next_node;

    def get_value(self):
        return self.value;

    def get_next_node(self):
        return self.next_node;

    def set_next_node(self, next_node):
        self.next_node = next_node;

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value);

    def get_head_node(self):
        return self.head_node;

    def insert_beginning(self, value):
        new_node = Node(value);
        new_node.set_next_node(self.head_node);
        self.head_node = new_node;

    def insert_end(self, value):
        tail = self.get_tail_node();
        tail.set_next_node(Node(value));

    def get_tail_node(self):
        curr = self.head_node;
        while (curr.get_next_node()):
            curr = curr.get_next_node()
        return curr;

    def stringify_list(self):
        current = self.head_node;
        output = "";
        while current.get_next_node() != None:
            output += str(current.get_value()) + "\n";
            current = current.get_next_node();
        output += str(current.get_value()) + "\n";
        return output;

    # Rewrite using single while-loop
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node();
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node());
                    current_node = None;
                else:
                    current_node = next_node;

ll = LinkedList(5);
ll.insert_beginning(2);
ll.insert_end(20);
ll.insert_end(25);
print(ll.stringify_list());