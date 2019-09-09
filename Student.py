#Name: Gaeun Lee
#UPI: glee217


#It collects the infromation of student
#It adds the marks how many answers they have got from the each labs
#It prints out ID, name, email, and list of marks in order
class Student:
    def __init__ (self, name, id, email):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__marks =[]
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
   
    def append_marks(self,mark):
        self.__marks.append(mark)
    def get_marks(self):
        return [mark for mark in self.__marks]
    def __str__(self):
        return str(self.__id) + ': ' + str(self.__name) + ', ' + str(self.__email) + ', ' + 'marks: ' + str(self.__marks)
