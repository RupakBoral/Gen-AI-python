from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    

dummy1 = {'id': 1, 'name': "rupak1", 'is_active': True}    
dummy2 = {'id': 2, 'name': "rupak2", 'is_active': 'False'} # even though False is a string, pydantic converts it to boolean
    
# user = User(id=dummy)
user1 = User(**dummy1)
user2 = User(**dummy2)

print(user1)
print(user2)


# PYDANTIC ONLY ACCEPTS KEYWORD ARGUMENTS
# It also tries to convert values into the correct data type

# 1️⃣ user = User(id=dummy)
# A single positional argument: id = dummy


# 2️⃣ user = User(*dummy)
# The * operator unpacks the dictionary keys, not the values.
# So, it gives error because no keyword arguments


# 3️⃣ user = User(**dummy) ✅
# The ** operator unpacks the dictionary into keyword arguments:
# id = 1, name = 'rupak', is_active = True