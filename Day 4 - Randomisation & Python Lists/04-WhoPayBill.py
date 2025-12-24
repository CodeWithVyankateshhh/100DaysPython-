# Who Pays the Bill?
import random
friends = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# random.choice selects a random element from the list 'friends'
# Here, it selects one friend to pay the bill
# Option 1: Using random.choice

payBill = random.choice(friends) # randomly selects one friend from the list
print(f"'{payBill}' is going to pay the bill today!")

# Option 2: Using random.randint
billPayerIndex = random.randint(0,len(friends)-1) # generates a random index within the range of the list
payBill2 = friends[billPayerIndex] # selects the friend at the generated index  
print(f"'{payBill2}' is going to pay the bill today!")

# Both options achieve the same result of randomly selecting a friend to pay the bill.

# option 3: Using random.sample
payBill3 = random.sample(friends, 1)[0] # randomly selects one friend from the list using sample
print(f"'{payBill3}' is going to pay the bill today!")
