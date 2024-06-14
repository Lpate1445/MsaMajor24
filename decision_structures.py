def main():


    a = 7
    b = 7
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    #print the appropriate letter grade based on the test score
    #A:100-90, B: 89-80, C: 79-70, D: 69-60, F 
    test_score = 77

    print("\nGrade Decision: 1")
    if test_score <=100 and test_score >=90:
        print(f"{test_score}--> A")
    elif test_score <=90 and test_score >=80:
        print(f"{test_score}--> B")
    elif test_score <=80 and test_score >=70:
        print(f"{test_score}--> C")
    elif test_score <=70 and test_score >=60:
        print(f"{test_score}--> D")
    else:
       print(f"{test_score}--> F")

    #Grade decisioln statement restructured 
    print("\nGrade Decision: 2")
    if test_score <=100 and test_score >=90:
        print(f"{test_score}--> A")
    elif test_score >=80:
        print(f"{test_score}--> B")
    elif test_score >=70:
        print(f"{test_score}--> C")
    elif test_score >=60:
        print(f"{test_score}--> D")
    else:
       print(f"{test_score}--> F")

    #create a decision structure to determine the season winter, spring, summer, fall based on the month 
    #Winter: 12,1,2; Spring: 3,4,5; Summmer 6,7,8; Fall 9,10,11; 
    #Ask the user to enter the number of the month 
    #Output the season based on the month
 
    #Create a function to return the season based on the month 
    #Input: month number 
    #Output: season name 
def main(): 
    while True:
        month_Entered = input("Enter month number 1-12")
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

main()
