filename = "/Users/Kota/Desktop/pcc_2e-master/chapter_10/pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")  # First 52 digits of pi
print(
    len(pi_string)
)  # Len is 1,000,002 because the million follows these two digits "3."


# Is your birthday contained in pi ?


birthday = input("Enter your birthday in the form of ddmmyy\n")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
