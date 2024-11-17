# Define a module function
def hours():
 print('Open 9-5 daily')

# Import the module interactively
import zoo
zoo.hours()

# 11.2 Import the module as menagerie and call its hours() function
import zoo as menagerie
menagerie.hours()

# 11.3 Import the hours() function from zoo directly and call it
from zoo import hours
hours()

# 11.4 Import the hours() function as info and call it
from zoo import hours as info
info()

