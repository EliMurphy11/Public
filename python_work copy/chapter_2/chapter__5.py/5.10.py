#  confirming everyone has a unique username
current_users = ['regina82', 'noobpro67', 'asherischeeks93', 'paxnation', 'elidaboi']
new_users = ['Regina82', 'coolguy123', 'asherischeeks93', 'gamergirl', 'paxnation']
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry {new_user}, that username is already taken. Please choose a different username.")
    else:
        print(f"Congratulations {new_user}, that username is available.")
