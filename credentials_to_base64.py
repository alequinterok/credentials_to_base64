import base64

# Function to read the file and return the lines as a list
def read_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Function to encode a username and password combination in base64
def encode_base64(username, password):
    # Join the username and password with ":" between them
    combination = f"{username}:{password}"
    # Encode the combination to bytes and then to base64
    combination_bytes = combination.encode('utf-8')
    combination_base64 = base64.b64encode(combination_bytes)
    # Decode it back to utf-8 to get the result as a string
    return combination_base64.decode('utf-8')

# Read the usernames and passwords from the files
usernames = read_file('Usernames_CISCO.txt')
passwords = read_file('Passwords_CISCO.txt')

# List to store the encoded combinations
base64_combinations = []

# Generate all possible combinations and encode them
for username in usernames:
    for password in passwords:
        base64_combination = encode_base64(username, password)
        base64_combinations.append(base64_combination)

# Write the encoded combinations to an output file
with open('user-pass_BASE64.txt', 'w') as f:
    for combination in base64_combinations:
        f.write(combination + '\n')

print("Process completed. The encoded combinations have been saved in 'user-pass_BASE64.txt'")
