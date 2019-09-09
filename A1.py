

from Student import Student
from Assessment import Assessment
from Histogram import Histogram


#This function reads the information of classlist.txt
#It can filter an error if the file is correct
#And returns in order of ID, name, e-mail and empty list for marks
def read_classlist(filename):
    try:
        student_list = []
        txt = open(filename, 'r')
        txt_read = txt.read()
        txt_list = txt_read.splitlines()
        txt.close()
        for x in range(len(txt_list)):
            txt_list[x] = txt_list[x].split(",")
        for y in range(len(txt_list)):
            student_list.append(Student(txt_list[y][0], txt_list[y][1], txt_list[y][2]))
        return student_list
        

        
    except FileNotFoundError:
        print("File",str(filename),"could not be opened")

#This function reads the information of solution.txt
#It can filter the error for the right type of file and the name.
#And returns the name of lab and answer of each questions but as the form of list
def read_solution(filename):
    try:
        lab_list = []
        txt = open(filename, 'r')
        txt_read = txt.read()
        txt.close()

        txt_list = txt_read.split('\n')

        for x in range(len(txt_list)):
            txt_list[x] = txt_list[x].split(":")
        for y in range(len(txt_list)):
            lab_list.append(Assessment(txt_list[y][0],txt_list[y][1]))
            
        return lab_list
    
    except NameError:
        print("File",str(filename),"could not be opened")
    except FileNotFoundError:
        print("File",str(filename),"could not be opened")


#It combines all the informations but shows two sections
#One is for how many students have got an answer for each questions in each labs
#The other shows how many questions they have got but for each students.
def read_data(assessment, classlist):
    
    questions = len(assessment.get_answer_list())
    histogram = Histogram(questions+1, questions)

    txt_name = assessment.get_name()+".txt"
    txt_file = open(txt_name, "r")
    txt_content = txt_file.read()
    txt_content = txt_content.split()
    txt_file.close()
  
    for r in range(len(txt_content)):
        field = txt_content[r].split(":")
        x = assessment.calculate_marks(field[1])
        histogram.append_marks(x)
        for y in range(len(classlist)):
            if r == y:
                classlist[y].append_marks(x)
    
    return histogram
        

#Adding line for convenience
def display_separator():
    lines = "-" * 40
    print(lines)



#Showing the read_data visually 
def main():
    class_list = read_classlist('classlist.txt')
    solution_list = read_solution('solution.txt')

    for x in solution_list:
        histogram = read_data(x, class_list)
        display_separator()
        print(x.get_name())
        histogram.draw()

    for y in class_list:
        print(y)
    display_separator()
    
main()
