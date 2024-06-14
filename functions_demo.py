#Function to add 2 numbers
#Input: (int)number_1, (int)number_2
#Output: (int)total
def add_numbers(number_1, number_2):
    total = number_1 + number_2
    c = 7
    return total 

def main():
    a = 5
    b = 4 
    c = 3
    #call the add_numbers function and assign the returned number
    answer = add_numbers(a, b)
    print(f"{a} + {b} = {answer}")
    print(f"Variable c = {c}")

main()

def get_month(month_Entered):
    while True:
        
        if month_Entered in ("12","1","2"):
                print("Winter")
                break
        elif month_Entered in ("3","4","5"):
                print("Spring")
                break
        elif month_Entered in ("6","7","8"):
                print("Summer")
                break
        elif month_Entered in ("9","10","11"):
                print("Fall")
                break    
        else:
            print("ERROR: Enter a number between 1 and 12")
            month_Entered = input("Enter month number 1-12")

def main():
    user_month = input("Enter month number 1-12")
    get_month(user_month)


main()
