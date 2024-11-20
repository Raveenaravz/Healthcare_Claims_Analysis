# Tuple - used to store multiple items in single variable.
# Tuple is ordered, unchangeable and allow duplicate values.
# Tuple is written with round brackets.

Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
print(Usa_states)

# len() - shows how many items a tuple has.
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
print(len(Usa_states))

# we can access the tuples by index number inside square brackets.
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
print(Usa_states[2])

# Negative indexing starts from end .
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
print(Usa_states[-1])

# Range of Indexes.
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
print(Usa_states[2:5])

# Range of negative indexes.
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
print(Usa_states[-5:-2])

# To check if an item is in tuple use 'IN' keyword.
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
if 'Boston' in Usa_states:
    print('yes, "Boston" is in the Usa_states')

# Tuples are unchangeable , but there is a workaround .
# We can convert tuple to a list and modify the values then convert list back to tuple.
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
largest_states = list(Usa_states)
largest_states[2] = "Texas"
Usa_states = tuple(largest_states)
print(Usa_states)

# Unpacking tuple - extract the values back into variavles
Usa_states = ('New York', 'Connecticut', 'Boston', 'New Hampshire', 'Ohio', 'Michigan', 'Arizona')
(state1,state2,state3,state4,state5,state6,state7) = Usa_states
print(state1)
print(state2)
print(state3)
print(state4)
print(state5)
print(state6)
print(state7)








