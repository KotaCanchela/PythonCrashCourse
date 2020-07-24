# Break a large dictionary into several lines for readability
# Add a comma after last key-value pair to be ready to add any future pairs
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

sarah_language = favourite_languages['sarah'].title()

print(f"Sarah's favourite language is {sarah_language}.")

print("The following languages have been mentioned: ")
for language in favourite_languages.values():
    print(language.title())

print(f"The following languages have been mentioned: "
      f"{[language for language in favourite_languages.values()]}")

# removing duplicates (python was mentioned twice before)

print("")
print("The following languages have been mentioned: ")
for language in set(favourite_languages.values()):    # set is a collection in which each item must be unique
    print(language.title())

# languages = {'python', 'ruby', 'c', 'python'} IS ALSO A SET
# print(languages) will return no duplicates
# IMPORTANT: IF YOU SEE BRACES BUT NO KEY-VALUE PAIRS. YOU'RE PROBABLY LOOKING AT A SET (does not retain info in order)

# 6-6 Polling

# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll.
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.

poll_applicants = ['jen', 'sarah', 'henry', 'james']

for applicant in poll_applicants:
    if applicant not in favourite_languages:
        print(f"{applicant.title()}, you have not yet taken the poll. "
              f"Please take the poll.")
    elif applicant in favourite_languages:
        print(f"Thank you {applicant.title()} for taking the poll.")
