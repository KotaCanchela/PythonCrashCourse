# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you

def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first.title()
    kwargs['last name'] = last.title()
    return kwargs


user_profile = build_profile('dakota', 'canchela',
                             height="5'6", age=22,
                             location='Paris')
print(user_profile)