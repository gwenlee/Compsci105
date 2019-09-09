
class Node:
    def __init__(self, new_value):
        self.value = new_value
        self.next = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next

    def set_value(self, new_value):
        self.value = new_value

    def set_next_node(self, new_next):
        self.next = new_next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0
        
    def add(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node
        
        self.__size += 1

        if self.tail == None:
            self.tail = new_node
        
    
    def append(self, value):
        new_node = Node(value)
        
        if self.tail == None:
            self.tail = new_node
            
        else:
            last_node = self.tail
            last_node.set_next_node(new_node)
            self.tail = new_node
            
        self.__size += 1

    def remove(self,value):
        found = False
        current = self.head
        previous = None
        
        while current != None and not found:
            if current.get_value() == value:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if found:
            if previous == None:
                self.head = current.get_next_node()
            else:
                previous.set_next_node(current.get_next_node())
                
     
        self.__size -= 1

    def size(self):
        return self.__size 
        

    def to_list(self):
        current = self.head
        my_list = []
        while current != None:
            my_list.append(current.get_value())
            current = current.get_next_node()
        return my_list




