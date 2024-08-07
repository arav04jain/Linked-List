class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:

    # self.head is the indicator to where the link list starts
    def __init__(self, *kwargs):
        self.head = None
        for element in kwargs:
            self.append(element)

    # Prints the Linked List
    def print_list(self):
        if self.head is None:
            return
        else:
            for x in range(self.length()):
                print(self.element_at(x))

    # Clears the list-Changes the head
    def clear(self):
        self.head = None

    # Gets the Index of a particular Element
    def index(self, element):
        current_node = self.head
        pos = 0
        while current_node:
            if current_node.data == element:
                return pos
            else:
                pos += 1

            current_node = current_node.next

    # Gives the Node on a particular index - Not to be used by the User
    def __node(self, index):
        if index + 1 <= self.length():
            current_node = self.head
            for iterate in range(index):
                current_node = current_node.next

            return current_node

        else:
            print("Index out of Range")

    # Gives the element on a particular Index
    def element_at(self, index):
        if index + 1 <= self.length():
            return self.__node(index).data
        else:
            print("Index out of Range")

    # Gives the length of the list
    def length(self):
        count = 0
        if self.head is None:
            return count
        else:
            current_node = self.head

            while current_node:
                count += 1
                current_node = current_node.next

        return count

    # Inserts Elements in the beginning of the Linked List
    def add_beg(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Inserts Element at the end of the linked list
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            end_node = self.__node(self.length() - 1)
            end_node.next = new_node

    # Inserts element at a particular index
    def insert(self, index, data):
        new_node = Node(data)

        if index == 0:
            self.add_beg(data)
        else:
            current_node = self.__node(index - 1)

            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print('Index not present')

    # Deletes the first element
    def delete_first(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        else:
            self.__node(self.length() - 2).next = None

    # Deletes a particular element at a certain Index
    def pop(self, index):
        if index == 0:
            self.delete_first()
        elif index == self.length() - 1:
            self.delete_last()
        else:
            self.__node(index - 1).next = self.__node(index + 1)

    # Deletes element by the Element
    def remove(self, element):
        self.pop(self.index(element))

    # Copies the list into another
    def copy(self):
        copy_list = List()
        for xx in range(self.length()):
            copy_list.append(self.element_at(xx))

        return copy_list

    # Merges 2 linked lists
    def extend(self, other_list):
        self.__node(self.length() - 1).next = other_list.head

    # Swaps on the basis of Index
    def swap_index(self, index1, index2):
        self.__node(index1).data, self.__node(index2).data = self.__node(
            index2).data, self.__node(index1).data

    # Swaps on the basis of data
    def swap_element(self, element1, element2):
        self.swap_index(self.index(element1), self.index(element2))

    # Uses Selection Sort for sorting the table
    def sort(self, reverse=False):
        if reverse == True:
            self.sort()
            self.reverse()
        else:
            for x in range(self.length()):
                current_min = x
                for y in range(x, self.length()):
                    if self.element_at(y) < self.element_at(current_min):
                        current_min = y
                self.swap_index(current_min, x)

    # Reverses the list
    def reverse(self):
        for x in range(self.length() // 2):
            self.swap_index(x, self.length() - x - 1)

    # Returns no. of times an element is repeated
    def count(self, element):
        count = 0
        for x in range(self.length()):
            if self.element_at(x) == element:
                count += 1

        return count

