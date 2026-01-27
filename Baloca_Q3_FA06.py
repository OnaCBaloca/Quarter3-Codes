

std = {"Name": "", "Age": 0, "Fav_subject": ""}

# Required Inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_subject = input("Enter your favorite subject: ")

std.update({"Name": name})
std.update({"Age": age})
std.update({"Fav_subject": fav_subject})

# Required Outputs
print("Student Record:")
print("Name:", std["Name"])
print("Age:", std["Age"])
print("Favorite Subject:", std["Fav_subject"])
