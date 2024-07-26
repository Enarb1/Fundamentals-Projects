import re


def validate_email(email):
    """
    Validate the email address using regex.
    :param email: str - Email address to validate
    :return: bool - True if valid, False otherwise
    """

    email_pattern = r'^[a-zA-Z0-9._-]+@[a-z0-9]+[.][a-z.]{2,6}$'
    return bool(re.match(email_pattern, email))


def validate_phone(phone):
    """
    Validate the phone number using regex.
    :param phone: str - Phone number to validate
    :return: bool - True if valid, False otherwise
    """
    phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(phone_pattern, phone))


def validate_postal_code(postal_code):
    """
    Validate the postal code using regex.
    :param postal_code: str - Postal code to validate
    :return: bool - True if valid, False otherwise
    """

    postal_code_pattern = r'^\d{5}$|^\d{5}-\d{4}$'
    return bool(re.match(postal_code_pattern, postal_code))


def main():
    """
    Main function to get user input and validate using the defined functions.
    """

    email = input("Enter your email address: ")
    if validate_email(email):
        print("The email address is valid.")
    else:
        print("The email address is invalid.")

    phone = input("Enter your phone number (XXX-XXX-XXXX): ")
    if validate_phone(phone):
        print("The phone number is valid.")
    else:
        print("The phone number is invalid.")

    postal_code = input("Enter your postal code (XXXXX or XXXXX-XXXX): ")
    if validate_postal_code(postal_code):
        print("The postal code is valid.")
    else:
        print("The postal code is invalid.")


if __name__ == "__main__":
    main()