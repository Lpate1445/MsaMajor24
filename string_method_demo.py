
def main():
    #Capitalize a string
    my_name = "lav"
    print(my_name.capitalize()) 

    #Make a string uppercase 
    print(my_name.upper())

    #Make a string lowercase
    last_name = "PATEL"
    print(f"{my_name.capitalize()} {last_name.lower()}")

    #Determine if a string starts with a set of characters
    print(my_name.startswith("L"))

    if(not my_name.startswith("l") and not my_name.startswith("K") ):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    #Determine if a string ends with a specidied set of characters 
    print(my_name.endswith("av"))

    #find a set of characters in a string
    print(my_name.find("l"))

    #loop through a string
    print("\n\n")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name(letter_index)}") 
    
    
    
    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of occurences of the word dog in sentence
    #expected output: 3 
    #start at the beginning of the string 
    #read the string until you find the first occurence of dog
    #add 1 to the number of found dogs
    #continue reading from the index: update the start index in the find method 
    index_number = 0
    dogs = 0
    while(not index_number == -1):
        index_number = sentence.find("dog", index_number + 1)
        dogs +=1 

    print(dogs - 1)

    #How to use the split method
    car_info = "Ferrari,f-50,2021,500000,4.8\n"

    car_data = car_info.split(",")
    print(car_data)


   



main()
