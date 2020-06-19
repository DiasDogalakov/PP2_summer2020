#Format the Result
"""
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:
"""
#Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)



#You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
#Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))



#Order the Result
#The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
