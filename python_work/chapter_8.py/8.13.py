def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info[' first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
# build a profile by calling build_profile() with your own first and last name and three other key-value pairs that describe you
my_profile = build_profile('eli', 'murphy',)
my_profile = build_profile('eli', 'murphy',
                           location='mckinney',
                           profession='baseball player',
                           hobby='musci listening')
