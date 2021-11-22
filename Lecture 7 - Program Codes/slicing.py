def main():
    my_string = "HELLO WORLD"
    print(my_string[0:5])  # HELLO
    print(my_string[6:11])  # WORLD
    print(my_string[3:-2])  # LO WOR
    print(my_string[0:11:2])  # HLOWRD

if __name__ == "__main__":
    main()