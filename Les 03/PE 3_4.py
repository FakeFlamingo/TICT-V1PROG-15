def newPassword(oldpassword, newpassword):
    if len(newpassword) > 5 and newpassword != oldpassword:
        return 'true'
    else:
        return 'false'


old = input('Wat is je oude password?')
new = input('Wat is je nieuwe wachtwoord?')

print(newPassword(old, new))
