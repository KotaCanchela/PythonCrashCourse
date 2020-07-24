# Return Values
# Instead of displaying output directly, it processes data and returns a value or set of values


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# The function therefore combines two names, adds a space between them
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
actor = get_formatted_name('will', 'smith')
print(actor)


# Making an argument optional
# If we want to add a middle name argument but it is optional
# We set middle name to an empty value


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician )
