# Use a while loop to modify a list as you work through it

# Start with users that need to be verified
# and an empty list to hold confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\n The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# To make this have input

print("\n\n")
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    ask = input("Please enter the name of a user to confirm: \n Once finished please type 'quit'\n\n")
    if ask in unconfirmed_users:
        print(f"\nVerifying user {ask.title()}...\n")
        confirmed_users.append(ask)
        unconfirmed_users.remove(ask)
    elif ask == 'quit':
        break
    else:
        print(f"{ask.title()} does not need to be confirmed.\n")
print("\n The following users have been confirmed:\n\t")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

print("\nThe following users remain unconfirmed:\n\t")

for unconfirmed_user in unconfirmed_users:
    print(unconfirmed_user.title())
