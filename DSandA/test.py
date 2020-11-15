class Classy():
    def __init__(self):
        self.items = []
    
# Function getClassiness is to calculate classiness points of each item
    def getClassiness(self):
        classiness_item = 0
        
        if len(self.items) > 0:
            for item in self.items:
                if item == "tophat" :
                    classiness_item += 2
                elif item == "bowtie" :
                    classiness_item += 4
                elif item == "monocle" :
                    classiness_item += 5
        return classiness_item

# Create function addItem to append new items
    def addItem(self, item):
        self.items.append(item)

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
