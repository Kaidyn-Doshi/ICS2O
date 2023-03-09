def calculate_birth_year(name, age, had_birthday):
    """
    Calculates the birth year based on the given age and whether the person had a birthday this year.
    """
    current_year = 2023
    birth_year = current_year - age
    
    if not had_birthday:
        birth_year -= 1
    
    return birth_year


name = input("What is your name? ")
age = int(input("What is your age? "))
had_birthday = input("Have you had a birthday this year? (y/n) ").lower() == "y"

birth_year = calculate_birth_year(name, age, had_birthday)

print(f"{name}, you were born in {birth_year}.")
