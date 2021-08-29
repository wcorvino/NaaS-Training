# Functions
def days_to_unitc(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days}  Days equals {number_of_days * 24}  hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days}  Days equals {number_of_days * 24 * 60}  minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        # conversion only for pos integers
        if user_input_number > 0:
            calculated_value = days_to_unitc(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("err.entered 0")
        else:
            print("err.entered neg")
    except ValueError:
        print("err.enter integer ot comma delimited list of values")


user_input_variable = "Enter value nn:text [#_of_Days:Conv_to_unit{minutes:hours}]\n"
