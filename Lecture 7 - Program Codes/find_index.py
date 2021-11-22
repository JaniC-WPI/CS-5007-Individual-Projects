def main():
    my_string = " HELLO WORLD"
    hello_string = "HELLO"
    hi_string = "HI"

    print(my_string.find(hello_string)) # Return the first index value that the string was found.
    print(my_string.find(hi_string))

    print(my_string.index(hello_string)) # Return the first index value that the string was found.
    # print(my_string.index(hi_string))

    # print(my_string.index(hi_string)) will raise an exception

    try:
        print(my_string.index(hi_string))
    except:
        print("Not Found")

if __name__ == "__main__":
    main()