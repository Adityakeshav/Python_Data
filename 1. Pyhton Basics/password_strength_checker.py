def is_strong_password(password):
    """This function will check the whether your password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '~!@#$%^&*()_+' for char in password):
        return False
    return True
password=input()
if(is_strong_password(password)):
    print("Your Password is Strong")

else:
    print("Your password is weak include Uppercase,lowercase,digit,Special Charcter as well")