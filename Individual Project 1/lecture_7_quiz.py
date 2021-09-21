def main():    
    cont = True
    while cont:
        num_1 = float(input("Enter the 1st number:"))
        num_2 = float(input("Enter the 2nd Number:"))

        SUM = num_1 + num_2
        PRODUCT = num_1 * num_2
        AVERAGE = SUM/2
    
        if (num_1 == 0 and num_2 == 0):
            print("Both Numbers are zero!")
            cont = False
         
        elif SUM > 200:
            print("SUM = ", SUM, "*")
            print("PRODUCT = ", PRODUCT)
            print("AVERAGE = ", AVERAGE)         
    
        else:
            print("SUM = ", SUM)
            print("PRODUCT = ", PRODUCT)
            print("AVERAGE = ", AVERAGE)
            
    

    
    

    

    

    
if __name__ == "__main__":
    main()