def camel_to_snake(variable_name):
    snake_case = [variable_name[0].lower()]
    for char in variable_name[1:]:
        if char.isupper():
            snake_case.extend(['_', char.lower()])
        else:
            snake_case.append(char)
    return ''.join(snake_case)

def main():
    user_input = input("Enter a variable name in camel case: ")
    snake_case_name = camel_to_snake(user_input)
    print(f"The corresponding snake case name is: {snake_case_name}")

if __name__ == "__main__":
    main()
