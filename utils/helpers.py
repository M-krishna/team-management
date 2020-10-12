from rest_framework.exceptions import ValidationError


def validate_phone_number(phone_number):
    if phone_number:
        mobile = phone_number
        if not mobile.isnumeric():
            raise ValidationError("Mobile number must contain numbers only")

        if len(mobile) > 15 or len(mobile) < 10:
            raise ValidationError("Mobile number should be between 10 and 15 digits!")
    return True
