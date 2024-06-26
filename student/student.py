class Student():

    def __init__ (self, first_name, last_name, major, credit_hours, gpa, student_id):

        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__student_id = student_id

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
    
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_major(self):
        return self.__major
    def set_major(self, new_major):
        self.__major = new_major

    def get_credit_hours(self):
        return self.__credit_hours
    def set_credit_hours(self, new_hours):
        try:
            self.__credit_hours = int(new_hours)
        except:
            print("Error: Credit hours must be an integer")

    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, new_gpa):
            self.__gpa = float(new_gpa)
            print("Error: GPA has to be a number under 4")

    def get_student_id(self):
        return self.__student_id
    def get_class_level(self, class_level):
        if -1 < self.__credit_hours <= 30:
            class_level = "Freshman"
        if 30 < self.__credit_hours <= 60:
            class_level = "Sophmore"
        if 60 < self.__credit_hours <= 90:
            class_level = "Junior"
        if self.__credit_hours > 90:
            class_level = "Senior"
            return class_level
    def update_credit_hours(self, additional_hours):
        if additional_hours > 0:
            try:
                self.__credit_hours += additional_hours
            except:
                print("Error: Additional hours must be a positive integer")
        else:
            print("Error: Additional hours must be a positive integer")
    def print_info(self):
        print(f"First name: {self.__first_name}")
        print(f"Last name: {self.__last_name}")
        print(f"Major: {self.__major}")
        print(f"Credit hours: {self.__credit_hours}")
        print(f"GPA: {self.__gpa}")
        print(f"Student ID number: {self.__student_id}\n")
