def main():
    # hard coded an example of a CSV format
    my_string = ""
    my_string = my_string + "1,2,3,4,5,6,7,8,9,10"  # row 1
    my_string = my_string + "\n"
    my_string = my_string + "100,200,300,400,500,600,700,800,900,1000"  # row 2
    my_string = my_string + "\n"
    my_string = my_string + "1000,2000,3000,4000,5000,6000,7000,8000,9000,10000"  # row 3
    print(my_string)

    # gives a list of rows
    # 1,2,3,4,5,6,7,8,9,10
    # 100,200,300,400,500,600,700,800,900,1000
    # 1000,2000,3000,4000,5000,6000,7000,8000,9000,10000

    row_list = my_string.split("\n")
    print()
    print(row_list) # ['1,2,3,4,5,6,7,8,9,10', '100,200,300,400,500,600,700,800,900,1000', '1000,2000,3000,4000,5000,6000,7000,8000,9000,10000']
    print()

    # for each row
    for i in row_list:
        column_list = i.split(",")
        print(column_list) #['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        # for each column
        for j in column_list:
            # print out value
            print(j, end=",") # 1,2,3,4,5,6,7,8,9,10,
        print()
        print()

if __name__ == "__main__":
    main()