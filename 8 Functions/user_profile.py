# Using arbitrary keyword arguments
# Sometimes you’ll want to accept an arbitrary number of arguments,
# but you won’t know ahead of time what kind of information will be passed to the function.
# In this case, you can write functions that accept as many key-value pairs as the calling statement provides.
# They are called **kwargs and are represented internally as a dictionary
# This is compared to *args which are represented as tuples


# One example involves building user profiles: you know you’ll get information about a user,
# but you’re not sure what kind of information you’ll receive.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything
    you know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


# Albert and einstein correspond with the first and last
# Location and field are both the arbitrary keywords found in **userinfo
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

# The double asterisks causes python to create an empty dictionary and pack values into it
# location and field are the keyword arguments


