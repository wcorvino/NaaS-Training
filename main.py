# Globals
k_sec_day = 24*60*60
unit = "Days"
unit_conv = "Seconds"

# Functions
def days_to_unitc(number_of_days):
    return f"{number_of_days} {unit} equals {number_of_days * k_sec_day} {unit_conv}"


def validate_and_execute():
    try:
        user_input_number = int(numb_of_days_element)
        # conversion only for pos integers
        if user_input_number > 0:
            calculated_value = days_to_unitc(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("err.entered 0")
        else:
            print("err.entered neg")
    except ValueError:
        print("err.enter integer ot comma delimited list of values")


# Run
user_input = ""
while user_input != "exit":
    user_input = input("Enter value  [Days]\n")
    list_of_days = user_input.split(",")

    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

    """
    print(type(user_input.split(",")))
    print(user_input.split(","))
    """
    for numb_of_days_element in set(user_input.split(",")):
        validate_and_execute()
