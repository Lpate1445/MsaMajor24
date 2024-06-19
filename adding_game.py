import random 
def get_level():
    while True:
            diff_level = int(input("Choose difficulty 1, 2, or 3: "))
            if diff_level == 1:
                print("Level 1 selected")
            elif diff_level == 2:
                    print("Level 2 selected")
            elif diff_level == 3:
                    print("Level 3 selected")
            else:
                print("Please enter the difficulty level")
                continue
    
def get_number_of_questions():
     number_of_questions = int(input("Please enter the number of questions you want t0 answer between 3 and 10: "))
     if number_of_questions in [3, 4, 5, 6, 7, 8, 9, 10]:
           return number_of_questions
     else: 
           print("ERROR: please enter a number between 3 and 10")
def main():
       user_level = int(get_level())
       user_number_of_questions = int(get_number_of_questions())
       if user_level == 1:
             for i in range (user_number_of_questions):
                   a = random.randint (0,9)
                   b = random.randint (0,9)
                   while True:
                    answer = int(input(f"{a} + {b}"))
                    if answer == a + b:
                          print("CORRECT!!!")
                    else:
                          print("WRONG!!!")



main()
