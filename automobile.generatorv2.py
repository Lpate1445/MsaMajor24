import automobile as auto 
#function load vehicle data from file 
#input: path to the file
#output: list of automobiles 
def load_vehicles(file_name):
    #create an empty list to store automobile data
    list_of_automobiles = []
    #open the file 
    auto_file = open(file_name, "r")

    #ignore the header data row in the file
    #auto_file.readline()
    next(auto_file)

    #read each line of the file in a for loop
    line_number = 1
    for line_of_data in auto_file:
        #increment line number by 1 
        line_number += 1

        #split each line at the comma to get values 
        vehicle_data = line_of_data.split(",")

        #check that vehicle_data contains 6 items
        #if not, raise error and skip that line of data 
        try:
            if len(list_of_automobiles)!= 6:
                raise Exception(f"There is an error in your data file on line {line_number}")
        except Exception as err:
            print(str(err))
            continue 

        #get the individual values form the resulting list 
        try:
            make = vehicle_data[0]
            model = vehicle_data[1]
            vin = vehicle_data[2]
           
            if vehicle_data[3].lower == "electric": 
                engine_size = 0
            else:
                engine_size = float(vehicle_data[3])
           
            owner = vehicle_data[4]
            year = int(vehicle_data[5])
        except Exception as err:
            print(f"Error:{err} on line {line_number}")
            continue

        
        
        #create automobile objects with the data
        new_auto = auto.Automobile(make, model, vin, engine_size, owner, year)
        
        #appened each automobile to the list of automobiles
        list_of_automobiles.append(new_auto)
    auto_file.close()

    pass

def main():
    #load a list of automobiles form data in a file
    automobile_list = load_vehicles("vehicle_data.csv")
    pass


main()
