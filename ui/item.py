class Item():
    global name
    global size

    def __init__(self, itemName, itemSize):
        self.setUpVariables(itemName, itemSize)
    
    def setUpVariables(self, itemName, itemSize):
        self.name = itemName
        self.size = itemSize
