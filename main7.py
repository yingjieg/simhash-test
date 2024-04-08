from simhash import Simhash, SimhashIndex

# Initialize an empty SimhashIndex
index = SimhashIndex([], k=3)

# Generate or receive new Simhash values dynamically
new_simhash_values = [
    (1, Simhash('How are you?')),
    (2, Simhash('How old are you?')),
    (3, Simhash('What is your name?')),
]

# Insert the new Simhash values into the index
for key, value in new_simhash_values:
    # print(type(value))
    index.add(key, value)

# Perform operations with the updated index
for value in index.get_near_dups(Simhash('what is your name')):
    print(value)

