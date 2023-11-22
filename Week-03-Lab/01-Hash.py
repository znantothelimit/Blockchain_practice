import hashlib

inString = input("Enter Data : ")

# print("Data : ", inString)

# Create a SHA-256 Hash object
sha256 = hashlib.sha256()

# Update Hash object with input string
sha256.update(inString.encode('utf-8'))

# Get HexaDecimal representation of hash
hashedString = sha256.hexdigest()

# Print Hashed string
# f-string
print(f"SHA-256 Hash ({inString}) : {hashedString}")
print("SHA-256 Hash (%s) : %s" %(inString, hashedString))
