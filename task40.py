#→ 40
def task40_password_strength(password):
    """
    Task 40:
    Write a function that checks password strength:
    - Length >= 8
    - Contains at least one digit
    - Contains at least one uppercase letter
    Return "Strong" if all conditions are met, otherwise "Weak".
    """
    
    password_has_required_length = len(password) >= 8
    password_has_atleast_one_digit = False
    password_has_atleast_uppercase = False

    for char in password:
        if char.isdigit():
            password_has_atleast_one_digit = True

    for char in password:
        if char.isupper():
            password_has_atleast_uppercase = True
    
    if password_has_required_length and password_has_atleast_one_digit and password_has_atleast_uppercase:
        return "Strong Password"

    else:
        return "Weak Password"

print(task40_password_strength("passwordA1"))
