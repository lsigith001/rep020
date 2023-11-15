# https://stackoverflow.com/questions/30556857/creating-a-static-class-with-no-instances
# Creating a static class with no instances

# That is, the Pythonic way would be:

# My module
elements = []

def add_element(x):
  elements.append(x)

# But if you want to mirror the structure of Java, you can do:

# My module
class World(object):
    elements = []
    @staticmethod
    def add_element(x):
        World.elements.append(x)


# You can also do this with @classmethod if you care to know the specific class (which can be handy if you want
# to allow the static method to be inherited by a class inheriting from this class):
#
#  My module
class World(object):
    elements = []
    @classmethod
    def add_element(cls, x):
        cls.elements.append(x)







# Hallo Änderung


# 03.01.2021 chg1 pc
# 04.01.2021 chg2 pc
# 04.01.2022 chg4 pc

# 04.01.2022 chg3 pc
# 04.01.2022  chg3 online 
# 04.01.2022 chg5 pc
