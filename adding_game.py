import random 
def get_level():
      while True:
            diff_level = (input("Choose difficulty 1, 2, or 3: "))
            if diff_level == '1':
                print("Level 1 selected")
                return diff_level
            elif diff_level == '2':
                    print("Level 2 selected")
                    return diff_level
            elif diff_level == '3':
                    print("Level 3 selected")
                    return diff_level
            else:
                print("Please enter the difficulty level")

def get_number_of_questions():
      while True:
            number_of_questions = (input("Please enter the number of questions you want to answer between 3 and 10: "))
            if number_of_questions in ['3', '4', '5', '6', '7', '8', '9', '10']:
                  return number_of_questions
            else: 
                  print("ERROR: please enter a number between 3 and 10")
def play_game(user_level):
      if(user_level == 1):
            a = random.randint(0,9)
            b = random.randint(0,9)
      if(user_level == 2):
              a = random.randint(10,99)
              b = random.randint(10,99)
      if(user_level == 3):
              a = random.randint(100,999)
              b = random.randint(100,999)
      counter = 0
      while True:
            try:
                  answer = int(input(f"{a} + {b} ="))
                  if answer == a + b:
                        print("CORRECT!!!")
                        return True 
                  else:
                        print("WRONG!!!")
                        counter += 1
                        if counter == 3:
                              print(f"Correct answer: {a} + {b} = {a + b}")
                              return False
            except:
                        print("WRONG!!!")
                        counter += 1
                        if counter == 3:
                              print(f"Correct answer: {a} + {b} = {a + b}")
                              return False 
                               
def main():
      user_level = int(get_level())
      number_of_questions = int(get_number_of_questions())
      correct = 0
      for i in range (number_of_questions):
              if play_game(user_level):
                     correct += 1
      percent_correct = correct * 100 / number_of_questions 
      print(f"You got {correct} out of {number_of_questions} questions correct: {percent_correct:.2f}%")

main()
