def get_user(username):
    db = {'alice': {'password': 'pass123', 'active': True}}
    return db.get(username)

username = 'alice'
password = 'pass123'

user = get_user(username)

if user and user['active'] and user['password'] == password:
    print('Login successful! Welcome,', username)
else:
    print('Login failed.')