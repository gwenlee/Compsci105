#Name: Gaeun Lee
#UPI: glee217

#It returns the maximum marks that student possibly get
#And it adds the marks if the student have got the answer
#Also, it can be shown with a better form but with asterisks
class Histogram:
    def __init__(self, range , max_mark):
        self.__range = range 
        self.__max_mark = max_mark
        self.__occurrence_list = [0] * self.__range
    def get_range(self):
        return self.__range
    def set_range(self, value):
        self.__range = value
    def get_max_mark(self):
        return self.__max_mark
    def set_max_mark(self, value):
        self.__max_mark = value
    def get_occurrence_list(self):
        return self.__occurrence_list
    def __str__(self):
        return 'max_mark: ' + str(self.__max_mark) + ', ' + 'occurrence: ' + str(self.__occurrence_list)
    def append_marks(self, value):
        if value > self.__max_mark:
            return 'value should be bigger than max mark'
        else:
            self.__occurrence_list[value] += 1
    def draw(self):
        for x in range(len(self.__occurrence_list)):
            print(x,':',(self.__occurrence_list[x])*'*', sep="")
