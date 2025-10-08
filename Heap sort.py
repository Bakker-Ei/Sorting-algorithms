array = []

while True:
    print (array)
    arraynumber = input("add elements to the array and press enter to continue: ")
    if arraynumber == "stop": 
        break
    elif arraynumber.startswith ("remove "):
        try:
            num_to_remove = int(arraynumber[len("remove "):])
            if num_to_remove in array:
                array.remove(num_to_remove)
            else:
                print("{int(arraynumber)} is not in the array.")
        except ValueError:
            print("Please enter a valid integer to remove.")
    else:
        try: 
            int(arraynumber)
            array.append(int(arraynumber))
        except ValueError:
            print("Please enter a valid integer, 'stop' to finish or 'remove ...' to remove a number.")