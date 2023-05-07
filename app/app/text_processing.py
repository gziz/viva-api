import re

def is_valid_string(string):
    # Check if the string length is greater than 1
    if len(string) <= 1:
        return False
    
    # Check if the string consists only of whitespace or non-word characters
    if re.search(r'^[\s\W]+$', string):
        return False
    
    # Check if the string consists of repeated characters
    if re.search(r'^(.)\1*$', string):
        return False
    
    # Additional checks or rules can be added here
    
    return True  # If none of the conditions matched, the string is considered valid
