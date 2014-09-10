def input_int(a, b):
    x = 0
    while x != "":
        x = input()
        if x.isdigit():
            if int(x) >= a and int(x) <= b:
                return x
        print("You should input a number between " + str(a) + " and " + str(b) + "!")
        print("Try once more or input empty line to cancel input check.")
            
        
