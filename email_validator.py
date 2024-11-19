import re

def is_valid_email(email):
    # Regular expression pattern for a basic email validation
    pattern = r"^[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$"
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function with different inputs
test_emails = [
    "example@domain.com",    # Valid
    "user.name@domain.com",  # Valid
    "username@domain",       # Invalid (missing top-level domain)
    "username@",             # Invalid (missing domain)
    "user@domain.comds",         # Invalid (domain too short)
    "@domain.com",           # Invalid (missing local part)
    "user@.com",             # Invalid (missing domain name)
    "user@@domain.com",      # Invalid (double @ symbol)
    "user@domain..com"       # Invalid (double dots)
]

for email in test_emails:
    print(f"'{email}' is valid: {is_valid_email(email)}")
