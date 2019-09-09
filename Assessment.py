#Name: Gaeun Lee
#UPI: glee217


#It shows the name of lab and answer for the questions
#And it calculate marks how many questions for student have got correctly
class Assessment:
    def __init__(self, name, answer_list):
        self.__name = name
        self.__answer_list = answer_list

    def get_name(self):
        return self.__name
    def get_answer_list(self):
        new = self.__answer_list.split(',')
        return new
    def __str__(self):
            return str(self.__name) + ": answer: " + str(self.__answer_list.split(','))
    def calculate_marks(self, data):
        sum1 = 0
        if len(self.__answer_list) > len(data):
            return 'Not enough answers'
        else:
            new_data = data.split(',')
            new_list = self.__answer_list.split(',')
            for x in range(len(new_list)):
                if new_list[x] == new_data[x]:
                    sum1 += 1             
      
        return sum1
