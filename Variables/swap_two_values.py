def swap_values(num_one, num_two):
    number_one = num_one
    number_two = num_two

    print("number_one", number_one)
    print("number_two", number_two)

    number_temp = number_one
    number_one = number_two
    number_two = number_temp

    print("number_one", number_one)
    print("number_two", number_two)


swap_values(3, 5)
