import student
from datetime import datetime
"""
Function to write error log file
Input: error message
Output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")

        #write error message to log file
        log_file.write(f"{datetime.now()}: {error_message}\n")

        #close log file
        log_file.close()
    except Exception as err:
        print(err)

    return


def load_students(file_name):
    list_of_students = []

    #create a file handler
    file = open(file_name, "r")

    #create variable to keep track of line in file that we are reading
    line_number = 0
    #read file line by line in for loop
    for line_of_data in file:
        line_number += 1
        #skip first line in csv file
        if line_number == 1:
            continue
        
        #split the line of data at the comma
        student_data = line_of_data.split(",")

        #handle errors in data format. line_of_data should have 6 items
        #if error in format then write a message to a log file and continue reading from the file
        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as err:
            write_to_error_log(str(err))
            continue

        #get student data and create a student object for each student
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
            student_id = student_data[5].strip()
        except:
            write_to_error_log(f"Error: {err} on line {line_number}")
            continue

        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, student_id)
        list_of_students.append(new_student)
    
    
    return list_of_students

#create a function called student_to_dictionary that creates a student dictionary for each student object
#Add student dictionaries to a list 
#Function to create a list of student dictionaries 
#Input: list of student objects
#Output: list of student dictionaries 
def student_to_dictionary(list_of_students):
    dictionary_list = []
    for student in list_of_students:
        dictionary = {
            "first name": student.get_first_name(),
            "last_name": student.get_last_name(),
            "id": student.get_student_id(),
            "major": student.get_major(),
            "gpa": student.get_gpa(),
            "class level": student.get_class_level(0),
        }
        dictionary_list.append(dictionary)
    return dictionary_list
    #loop through the list of students : for loop 
    #create a dictionary for each student object

def get_student_dictionaries():
    #Create 2 instances of Student
    list_of_students = load_students("students.csv")

    student_dictionaries = student_to_dictionary(list_of_students)

    return student_dictionaries
