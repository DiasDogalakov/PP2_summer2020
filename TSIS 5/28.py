import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)
