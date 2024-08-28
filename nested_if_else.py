# 2 states -> State1 and State2
# In State1, >18 can vote
# In State2, >20 can vote

# take state as an input
state = input("Enter your state:")

# take age as an input
age = int(input("Enter your age:"))

# display whether they can vote or not

if state == "State1":
    if age > 18:
        print("Can vote in state 1")
    else:
        print("Cannot vote in state 1")
else:
    if age > 20:
        print("Can vote in state 2")
    else:
        print("Cannot vote in state 2")