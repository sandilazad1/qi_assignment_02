def find_the_max_of_three_number(num_one,num_two,num_three):
    if(num_one < num_two):
        if(num_three < num_two):
            print(num_two)
        else:
            print(num_three)
    else:
        print(num_one)


find_the_max_of_three_number(9,9,790)