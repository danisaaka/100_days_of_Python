# Functions with Outputs.
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("ISAAKA","isaaka")
# print(formated_string)

print(format_name(input("What is your first name?\n"),input("What is your last name?\n")))