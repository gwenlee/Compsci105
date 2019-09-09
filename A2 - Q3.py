
def hashing(list_of_keys, size, probing, q):
    
    new_list = []
    
    while len(new_list) != size:
        new_list += [None]

    #All of probing shares the common equation which is key % size    
    for key in list_of_keys:
        x = key % size
        
        if new_list[x] == None:
            new_list[x] = key
    
        else:
            if probing == 'linear':
                y = x
                i = 1
                while new_list[y] != None:
                    y = (x + i) % size
                    i += 1
                new_list[y] = key
                
            elif probing == 'quadratic':
                y = x
                i = 1
                while new_list[y] != None:
                    quadratic = i*i
                    y = (x + quadratic) % size
                    i += 1
                new_list[y] = key


            elif probing == 'double':
                step_value = q - (key % q)
                y = (x+step_value) % size
                
                if new_list[y] == None:
                    new_list[y] = key
                else:
                    while new_list[y] != None:
                        y = (y + step_value)%size
                    new_list[y] = key

    return new_list

        
   
values = [25,19,32,6,12]
linear = hashing(values, 7, 'linear', None)
quadratic = hashing(values, 7, 'quadratic', None)
double = hashing(values, 7, 'double', 5)
print('Linear =\n', linear)
print('Quadratic =\n', quadratic)
print('Double =\n', double)
