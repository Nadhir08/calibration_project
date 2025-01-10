def get_calibration_value(line):
    
    """Extract first and last digit from a line to form a two-digit number."""
    
    digits = [char for char in line if char.isdigit()]
    if not digits:
        return 0
    first_digit = digits[0]
    last_digit = digits[-1]
    return int(first_digit + last_digit)

def calculate_total_calibration(document):
    
    """Calculate sum of calibration values for all lines."""
    
    total = 0
    for line in document.strip().split('\n'):
        value = get_calibration_value(line)
        total += value
    return total

# Read the document content from a file

with open('data.txt', 'r') as file:
    document_content = file.read()

# Calculate and print result

result = calculate_total_calibration(document_content)
print(f"The sum of all calibration values is: {result}")