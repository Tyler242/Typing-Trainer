"""
CSE 212 Lesson 5A 

Demonstrate how sets work.
"""

# Create an empty set of names
names = set()
print("Empty set: {}\n".format(names))

# Create a set of two names: Bob and Tim
names = {"Bob", "Tim"}
name_list = ["Bob", "Tim"]
print("Set with Bob and Tim: {}\n".format(names))
print("Set with Bob and Tim: {}\n".format(name_list))

# Add a Sue to the set
names.add("Sue")
name_list.append("Sue")
print("After adding Sue (notice not in order): {}\n".format(names))
print("After adding Sue (notice not in order): {}\n".format(name_list))

# Add Bob again (duplicate)
names.add("Bob")
name_list.append("Bob")
print("After tyring to add Bob again: {}\n".format(names))
print("After tyring to add Bob again: {}\n".format(name_list))

# Check for membership
for i in range(100000000):
  names.add("a" + str(i))
  name_list.append("a" + str(i))
find_name = input("Enter a name: ")
if find_name in names:
    print("In the Set.\n")
if find_name in name_list:
    print("In the Set.\n")
else:
    print("Not in the Set.\n")

# Remove Bob from the set
#names.remove(find_name)
#name_list.remove(find_name)
#print("After removing Bob: {}\n".format(names))
#print("After removing Bob: {}\n".format(name_list))
