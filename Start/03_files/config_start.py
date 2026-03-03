# read the contents of configuration files
import configparser


# TODO: Create the configuration parser
parser = configparser.ConfigParser()

# TODO: Read the configuration file
parser.read("config.cfg")

# TODO: print the sections
print(parser.sections())
print(parser.has_section("Section 1"))
print(parser.has_section("Section 31"))

# TODO: Access one of the default values
print()
using_time_travel = parser['DEFAULT']['UseTimeTravel']
print(using_time_travel)
print(type(using_time_travel))
print()

# TODO: Demonstrate the getXXX convenience functions
obd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
print(obd)

speed = parser['DEFAULT'].getfloat('Ship Speed')
print(speed)

# TODO: Access a non-existent value
try:
  title = parser['Section 3']['Title']
  print(title)
except KeyError as err:
  print("There is no:", err)