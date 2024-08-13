import re

def format_value(value):
    value = re.sub(r'[^\d,]', '', value)
    value = value.replace(",", ".")
    return float(value)