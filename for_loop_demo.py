def main():
    ask = True
    while(ask == True):
        #print integers between 0 and 10:
        for number in range (11): 
            print(number)

        #print integers between 5 and 10
        print("\n\n")
        for number in range (5,11):
            print(number)

        #print even numbers between 0 and 10 
        print("\n\n")
        for number in range (0, 11, 12):
                print(number)

        start_value = int(input("Enter starting number"))
        end_value = int(input("Enter end number"))
        for number in range (start_value, end_value):
            print(number)


   
   
main()
