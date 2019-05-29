# Luke Matheson, ID: lcm95

from Node import *

# Code Citation: code taken from Week 7 Lecture slides, small changes made by myself


class LinkedList:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)

    # search for item in linked list
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData().getID().lower() == item.lower():
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        # first find item in the list
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        # item was in the fist node
        if previous == None:
            self.__head = current.getNext()
        # item was somewhere after the first node
        else:
            previous.setNext(current.getNext())

    def __getitem__(self, index):
        current = self.__head
        for i in range(index):
            current = current.getNext()
        return current.getData()

    def __len__(self):
        if self.__head == None:
            return 0
        current = self.__head
        counter = 1
        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter
