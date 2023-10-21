def is_valid_email(*email):
    if email.count('@') != 1:   # Counting '@' Symbol:
        return False
    local_part, domain_part = email.split('@')  #Splitting Local Part and Domain Part
    if not local_part or not domain_part:       #Checking Non-Empty Parts:
        return False
    domain, tld = domain_part.split('.')        #Splitting Domain and TLD(top level domain)
    if not domain or not tld:                   #Checking Non-Empty Domain and TLD
        return False
    return True
# Example usage
email1 = "user@example.com"
email2 = "invalid_email@.com"
OBJ1=is_valid_email()
print(OBJ1)


"""e
email3 = "another.user@domain.co"
print(f"Is '{email1}' a valid email? {is_valid_email(email1)}")
print(f"Is '{email2}' a valid email? {is_valid_email(email2)}")
print(f"Is '{email3}' a valid email? {is_valid_email(email3)}")"""
