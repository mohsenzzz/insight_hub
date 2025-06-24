from rest_framework.exceptions import ValidationError



def validate_argument_type(filed_type:str, value):
    if filed_type == 'string' and type(value) is not str:
        raise ValidationError(f"type of {value} does not match.")
    elif filed_type == 'integer' and type(value) is not int:
        raise ValidationError(f"type of {value} does not match.")
    elif filed_type == 'float' and type(value) is not float:
        raise ValidationError(f"type of {value} does not match.")