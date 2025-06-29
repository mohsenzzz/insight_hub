




def convert_value_type(value: str, type_str: str):

        try:
            if type_str == 'string':
                return str(value)
            elif type_str == 'integer':
                return int(value)
            elif type_str == 'float':
                return float(value)
            elif type_str == 'boolean':
                return value.lower() in ('true', '1', 'yes')
            else:
                raise ValueError(f"Unsupported type: {type_str}")
        except Exception as e:
            raise ValueError(f"Invalid value '{value}' for type '{type_str}': {e}")
