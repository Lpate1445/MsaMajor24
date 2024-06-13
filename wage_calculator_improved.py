def main():
        while True: 
            bad_input_1 = True
            bad_input_2 = True 

            while(bad_input_1 == True):
                try:
                    get_hours_worked= float(input("Enter Hours Worked:"))
                    if get_hours_worked > 24:
                        print("ERROR: Hours worked cannot be greater than 24")
                        continue
                    if get_hours_worked < 0:
                        print("ERROR: Hours worked cannot be less than 0")
                        continue 

                    break 
                except:
                    print("ERROR")
            while(bad_input_2 == True):
                try:
                    hourly_wage = float(input("Enter the hourly wage:"))
                    if hourly_wage < 1:
                        print("ERROR, hourly wage cannot be lower than 0")
                        continue 
                    else: break 
                except:
                    print("ERROR")

            daily_wage = (get_hours_worked * hourly_wage)
            yearly_wage= (daily_wage * 350) 
            yearly_tax= (yearly_wage * 0.12) 
            wage_after_tax_deduction = (yearly_wage - yearly_tax)




            print("Pay Advice")
            print("-------------")
            print("Hours Worked", get_hours_worked)
            print("Hourly Wage = $", hourly_wage )
            print("Wages Before Taxes = $",yearly_wage)
            print("Tax Amount = $", yearly_tax)
            print(f"Annual Wage After Taxes = $", wage_after_tax_deduction)

            #Ask user if they want to run calculator agian 
            run_again = input("Do you want to run the program again")
            
            #if run_again = y then return code, else end the program 
            if run_again == "y":
                continue
            else:
                print("Program ending")
                break 
   


main()
