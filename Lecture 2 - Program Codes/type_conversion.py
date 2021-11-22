def main():
    float_value = 5.5
    int_value = 5
    complex_value = 5 + 5j
    string_value = "5"
    string_value2 = "five"
    bool_value = True # True = 1; False = 0

    print("Type of float_value = " + str(type(float_value)) + ": " + str(float_value))
    print("Type of int_value = " + str(type(int_value)) + ": " + str(int_value))
    print("Type of complex_value = " + str(type(complex_value)) + ": " + str(complex_value))
    print("Type of string_value = " + str(type(string_value)) + ": " + str(string_value))
    print("Type of string_value2 = " + str(type(string_value2)) + ": " + str(string_value))
    print("Type of bool_value = " + str(type(bool_value)) + ": " + str(bool_value))

    print()

    float_to_int = int(float_value)
    string_to_int = int(string_value)
    bool_to_int = int(bool_value)
    # string2_to_int = int(string_value2) results in error, "five"
    # complex_to_int N/A

    print("Type of float_value converted to int = " + str(type(float_to_int)) + ": " + str(float_to_int))
    print("Type of string_value converted to int = " + str(type(string_to_int)) + ": " + str(string_to_int))
    print("Type of bool_value converted to int = " + str(type(bool_to_int)) + ": " + str(bool_to_int))

    print()

    int_to_float = float(int_value)
    string_to_float = float(string_value)
    bool_to_float = float(bool_value)
    # string2_to_float = float(string_value2) results in error
    # complex_to_float =N/A

    print("Type of int_value converted to float = " + str(type(int_to_float)) + ": " + str(int_to_float))
    print("Type of string_value converted to float = " + str(type(string_to_float)) + ": " + str(string_to_float))
    print("Type of bool_value converted to float = " + str(type(bool_to_float)) + ": " + str(bool_to_float))

    print()

    int_to_string = str(int_value)
    float_to_string = str(float_value)
    complex_to_string = str(complex_value)
    bool_to_string = str(bool_value)

    print("Type of int_value converted to string = " + str(type(int_to_string)) + ": " + str(int_to_string))
    print("Type of float_value converted to string = " + str(type(float_to_string))+ ": " + str(float_to_string))
    print("Type of complex_value converted to string = " + str(type(complex_to_string)) + ": " + str(complex_to_string))
    print("Type of bool_value converted to string = " + str(type(bool_to_string)) + ": " + str(bool_to_string))

    print()

    int_to_complex = complex(int_value)
    float_to_complex = complex(float_value)
    string_to_complex = complex(string_value)
    bool_to_complex = complex(bool_value)
    # string2_to_complex = complex(string_value2) results in error

    print("Type of int_value converted to complex = " + str(type(int_to_complex)) + ": " + str(int_to_complex))
    print("Type of float_value converted to complex = " + str(type(float_to_complex)) + ": " + str(float_to_complex))
    print("Type of string_value converted to complex = " + str(type(string_to_complex)) + ": " + str(string_to_complex))
    print("Type of bool_value converted to complex = " + str(type(bool_to_complex)) + ": " + str(bool_to_complex))

    print()

    int_to_bool = bool(int_value)
    float_to_bool = bool(float_value)
    string_to_bool = bool(string_value)
    complex_to_bool = bool(complex_value)
    # string2_to_bool = bool(string_value2) results in error

    print("Type of int_value converted to bool = " + str(type(int_to_bool)) + ": " + str(int_to_bool))
    print("Type of float_value converted to bool = " + str(type(float_to_bool)) + ": " + str(float_to_bool))
    print("Type of string_value converted to bool = " + str(type(string_to_bool)) + ": " + str(string_to_bool))
    print("Type of complex_value converted to bool = " + str(type(complex_to_bool)) + ": " + str(complex_to_bool))

if __name__ == "__main__":
    main()