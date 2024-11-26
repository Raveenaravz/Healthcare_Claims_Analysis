# Dictionaries are used to store data values in key : value pairs.
# values in dictionaries are ordered, changeable and no duplicates allowed.
# Dictionaries are written in curly brackets and have keys and values.

Company_CEO = {
"Apple": "Tim_cook",
"Tesla": "Elon_musk",
"Nvidia": "Jensen_Huang",
"Microsoft": "Sathya_nadella",
"Amazon": "Jeff_Bezos"
}

print(Company_CEO)

# Access Dictionary items by referring the key name in square brackets
Company_CEO = {
"Apple": "Tim_cook",
"Tesla": "Elon_musk",
"Nvidia": "Jensen_Huang",
"Microsoft": "Sathya_nadella",
"Amazon": "Jeff_Bezos"
}
x = Company_CEO["Tesla"]
print(x)

# get() also give particular item by referring key value in square brackets
Company_CEO = {
"Apple": "Tim_cook",
"Tesla": "Elon_musk",
"Nvidia": "Jensen_Huang",
"Microsoft": "Sathya_nadella",
"Amazon": "Jeff_Bezos"
}
x = Company_CEO.get("Tesla")
print(x)

# keys()- returns list of all keys in the dictionary
Company_CEO = {
"Apple": "Tim_cook",
"Tesla": "Elon_musk",
"Nvidia": "Jensen_Huang",
"Microsoft": "Sathya_nadella",
"Amazon": "Jeff_Bezos"
}
x = Company_CEO.keys()
print(x)

# add new key value pair to the dictionary by writing in square brackets
Company_CEO = {
"Apple": "Tim_cook",
"Tesla": "Elon_musk",
"Nvidia": "Jensen_Huang",
"Microsoft": "Sathya_nadella",
"Amazon": "Jeff_Bezos"
}
x = Company_CEO.keys()
print(x)  # before change
Company_CEO["Meta"] = "Mark_Zuckerberg"
print(x) #after the change

# update()- help to add new key value pair to the dictionary
Company_CEO = {
"Apple": "Tim_cook",
"Tesla": "Elon_musk",
"Nvidia": "Jensen_Huang",
"Microsoft": "Sathya_nadella",
"Amazon": "Jeff_Bezos"
}
Company_CEO.update({"Meta" : "Mark_zukerberg"})
print(Company_CEO)


