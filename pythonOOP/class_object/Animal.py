class Animal:
    def lion(self, hair, weight ):
        self.hair = hair
        self.weight = weight
        return self.weight

lion1 = Animal()
lion1.lion('striped', 90.1)
print(lion1.hair, lion1.weight)