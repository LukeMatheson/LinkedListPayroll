# Luke Matheson, ID: lcm95
# Class Code Citation: code used from Week 7 lecture slides


class Node:
    def __init__(self, data, nextNode=None):
        self.__data = data
        self.__next = nextNode

    def getData(self):
        return self.__data

    def getID(self):
        return self.__data.getID()

    def getNext(self):
        return self.__next

    def setData(self, d):
        self.__data = d

    def setNext(self, n):
        self.__next = n

    def __str__(self):
        return str(self.__data)
