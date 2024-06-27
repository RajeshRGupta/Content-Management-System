from django.core.exceptions import ValidationError
import re

def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")

def validate_phone(phone):
    if not phone.isdigit():
        raise ValidationError('Phone number must only contain numeric digits.')
    if len(phone) != 10:
        raise ValidationError('Phone number must be exactly 10 digits long.')

def validate_pincode(pincode):
    if not pincode.isdigit():
        raise ValidationError('Phone number must only contain numeric digits.')
    if len(pincode) != 6:
        raise ValidationError('Phone number must be exactly 10 digits long.')
