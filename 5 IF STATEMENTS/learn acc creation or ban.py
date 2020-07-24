banned_users = ['andrew', 'carolina', 'david']
user = str(input('Please enter your name\n'))

if user.lower() not in banned_users:
    print(f"{user.title()}, your account has been created")
elif user.lower() in banned_users:
    print(f"{user.title()}, unfortunately your account is banned")