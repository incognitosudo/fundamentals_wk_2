import my_module #Makes code available to be used in this file.

my_module.greet("Albert Einstein")
print("My favorite ice cream flabor is ", my_module.flavor)


#or

from my_module import greet, flavor  #help saves memory

greet("Vanderbilt")
print(flavor)
