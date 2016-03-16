
class fish:
    # initializer for your objects
    # doubel underscore indecates a sepecial interaction don't worry about them
    def __init__(self, name):
        self.name = name
        self.size = 0

    def setSize(self, sizeIn):
        self.size = sizeIn

    def about(self):
        print ("name:", self.name )
        print ("size:", self.size )


newFish = fish("Jerry")
newFish.about()
print("~~~~~~~~~~~")
newFish.setSize(4)
newFish.about()
