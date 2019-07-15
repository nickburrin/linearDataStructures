from LinkedList import LinkedList;

ll = LinkedList(5);
ll.insert_beginning(2);
ll.insert_end(20);
ll.insert_end(25);
print(ll.stringify_list());

ll.remove_node(25);
print(ll.stringify_list());