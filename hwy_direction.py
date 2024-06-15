#create a program that accepts a hwy number and outputs the direction 
#User enters: 95 
#Output: "Interstate 95 runs South to North"
def main():
    while True:
        try:
            highway_number = int(input("Enter a interstate number: "))
            if highway_number < 0:
                print("ERROR: Please enter a positive integer")
                continue 
            if (highway_number % 2 == 0): 
                print(f"Interstate {highway_number} goes East to West")
                break
            else:
                print(f"Interstate {highway_number} goes North to South")
                break
        except:
            print("ERROR: Please enter an integer")
            continue
main()
        
