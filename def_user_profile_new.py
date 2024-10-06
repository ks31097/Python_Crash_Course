def build_profile(first, last, **user_info): # **kwargs
    """Creating a dictionary"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)

user_profile = build_profile('my_name', 'my_surname', country='some country', street='some street', telephone='number',)
print(user_profile)