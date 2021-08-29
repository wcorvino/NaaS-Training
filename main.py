k_sec_day = {24*60*60}
unit = "Days"
unitc = "Seconds"

def days_to_unitc(number_of_days):
    return f"{number_of_days}{unit}equals{number_of_days*k_sec_days}{unitc}"

def validate_and_execute():
    try:
        user_input_number=int(num_of_days_element)
        if user_input_number>0:
            calculated_value=days_to_unitc(user_input_number)
            print(calculated_value)
        elif use_input_number == 0:
            print("err.entered 0")
        else:
            print("err.entered neg")
    except ValueError:
        print("err.enter integer ot comma delimited list of values")


user_input=""
while user_input!= "exit":
    user_input = input("Enter value  [Days]\n")
    print(type(user_input.split(",")))
    print(user_input.splt(","))
    for numb_of_days_element in user_input.splt(","):
        validate_and_execute()

