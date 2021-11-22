def main():
    my_string = "1 2 3 4 5 6 7 8 9 10"
    print(my_string)

    my_string2 = my_string.replace(" ", ",")
    print(my_string2)

    my_string3 = my_string.replace(" ", ",", 5)
    print(my_string3)

    print(id(my_string))
    print(id(my_string2))
    print(id(my_string3))

if __name__ == "__main__":
    main()
