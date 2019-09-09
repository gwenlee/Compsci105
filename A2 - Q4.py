
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_left(self):
         return self.left

    def get_right(self):
         return self.right

    def get_data(self):
         return self.data

    def set_data(self, data):
         self.data = data

#Since insert_left changes the order of insertion as backward, I used
#insert_tree_left() function which allocates the left leaf to the node directly 
    def insert_tree_left(self, left_tree):
        self.left = left_tree

            
#The reason why i used is similar as insert_tree_left() funcion
    def insert_tree_right(self, right_tree):
        self.right = right_tree
    
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t



#I divided into two functions, converting the give flat list into tree
#And print this tree into nested list 
def convert_flat_to_nested_list(flat_list):
    tree = convert_flat_to_tree(flat_list, 1)
    list1 = convert_tree_to_nested(tree)

    return list1

      
#Converting flat list into tree
def convert_flat_to_tree(flat_list, index):
    
    if index >= len(flat_list) or flat_list[index] == None:
        return None
    
    else:
        a = BinaryTree(flat_list[index])
        
        left = index*2 
        right = index*2 + 1
        
        a.insert_tree_left(convert_flat_to_tree(flat_list,left))
        a.insert_tree_right(convert_flat_to_tree(flat_list,right))
            
        return a
        
#Converting tree into nested list
def convert_tree_to_nested(tree):

    if tree == None:
        return None
    
    else:
        my_list = []
        my_list.append(tree.get_data())
        my_list.append(convert_tree_to_nested(tree.get_left()))
        my_list.append(convert_tree_to_nested(tree.get_right()))
        
    return my_list
    

##test implementation
flat_list = [None, 10, 5, 15, None, None, 11, 22]

nested_list = convert_flat_to_nested_list(flat_list)
print(nested_list)
