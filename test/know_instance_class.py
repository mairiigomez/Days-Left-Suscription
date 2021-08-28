"""Trying to know the instance of a class so a can refer to them later on"""

class Thingy(object):
    instances = []

    # The init method is just to apped them
    def __init__(self, name, id_):
        self.name = name
        self.id = id_
        self.instances.append(self)

# This function is to create the instance 
# so if we want to give atributes to the instance send them here 
def waste_time_and_memory(name, id_):
    t = Thingy(name, id_)

for i in range(5):
    waste_time_and_memory('a','b')

print(Thingy.instances)