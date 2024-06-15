def main():
    Amount_left = 50 
    while True:
            print(f"Vending Machine\n----------------- \nAmount Due: {Amount_left}")
            ask_for_money = input("Please enter a coin here: ")
            if ask_for_money in ("1","5","10","25"):
                Amount_left = Amount_left - int(ask_for_money)
            else:
                 print("Invalid denominations")
            if Amount_left == 0:

            elif Amount_left < 0: 
                change_owed 
                print(f"Change owed {change_owed}")    
                
            print(f"Change owed {Amount_left}")

main()
