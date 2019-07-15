from Node import Node;

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

    def get_node_with_value(self, value):
        curr = self.head_node;
        while curr.get_value() != value:
            if curr.get_next_node() == None:
                print('** Could not find node with value: {} **'.format(value));
                return None;
            curr = curr.get_next_node();
        return curr;

    def stringify_list(self):
        current = self.head_node;
        output = "";
        while current.get_next_node() != None:
            output += str(current.get_value()) + "\n";
            current = current.get_next_node();
        output += str(current.get_value()) + "\n";
        return output;

    def remove_node(self, value_to_remove):
        print('Removing node with value: {}'.format(value_to_remove));
        
        current = self.head_node;
        next = current.get_next_node()
        if current.get_value == value_to_remove:
            self.head_node = next;
        else:
            while next.get_value() != value_to_remove:
                current = next;
                next = next.get_next_node();
                if next == None:
                    print('No node to remove with value: {}'.format(value_to_remove));
                    return;
            current.set_next_node(next.get_next_node());