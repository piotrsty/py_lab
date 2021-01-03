customer = {
"name": "Jon Doe",
"email": "jon.doe@gamil.com",
"age": 30,
"is_verified": True

}
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
#print(customer["birthdate"])
#print(customer["name"])
#print(customer.get("dupa", "blabla"))

#exercise

phone = input("phone: ")
digit_mapping = {
"1": "one",
"2": "two",
"3": "three",
"4": "four",
"5": "five"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)


