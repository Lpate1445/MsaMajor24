#write a program to convert pounds to kilograms
#write a function to get a positive number from the user 
def get_positive_float_input():
  #ask a user to answer their weight in pounds, and validate correct input 
  #if bad input, reprompt the user
  user_weight= 0
  #bad_input= True 
  while(True):
    try:
      user_weight= float(input("Enter your weight in pounds:"))
      #check if user weight is > 0 if not then reprompt the user 
      if user_weight <= 0: 
        print("ERROR: Enter a number greater than 0")
        continue 

      break 
    except:
     print("ERROR: Please enter a number")

  return user_weight


#INPUT
#get weight from the user 
user_weight = get_positive_float_input
 



#PROCESSING
#use a conversion to coinvert pounds to kilos :2.205 lbs =1kg
lbs_to_kgs_conversion = 2.205 
user_weight_in_kg= user_weight / lbs_to_kgs_conversion

#OUTPUT
#print output to the user
#You weight XXXX kgs 
print(f"You weight {user_weight_in_kg:.2f}kgs")