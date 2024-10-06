import class_user as user

sys_admin = user.Admin('first_name', 'second_name', 4, 'Super country')
sys_admin.orivileges.show_privileges()
print(sys_admin.greet_user())