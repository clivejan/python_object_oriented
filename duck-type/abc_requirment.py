from collections.abc import Container

# display the required implements for a class
print(Container.__abstractmethods__)

# display what signature should be implemented
help(Container.__contains__)
