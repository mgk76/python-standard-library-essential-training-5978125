# String formatting methods and best practices
from string import Template
import datetime

# TODO: Using Template strings
the_str = "The quick brown $animal $action over the lazy dog"
the_template = Template(the_str)
output_str = the_template.substitute(animal="fox", action="jumped")
print(output_str)

print()

#As above but use a dict as a parameter to substitute
args = {
  "animal" : "cow",
  "action" : "walked",
}
output_str = the_template.substitute(args)
print(output_str)

# TODO: Using str.format()
str1 = "foo"
val1 = 123

print("Output: {}, {}".format(str1, val1))
print("Output: {1}, {0}".format(str1, val1))
print("Output: {var2}, {var1}".format(var1=str1, var2=val1))
print("Output: {var2:x}, {var2:X}, {var1}".format(var1=str1, var2=val1))

print()

# TODO: Using interpolation with f-strings in Python 3.6
product = "Widget"
price = 19.99
tax = 0.07
nyd = datetime.datetime(2027,1,1)

print(f"{product.upper()} has a price of {price}, with tax {tax:.2%} the total is {round(price + (price * tax),2)}")
print(f"But only on: {nyd:%B %d, %Y}")