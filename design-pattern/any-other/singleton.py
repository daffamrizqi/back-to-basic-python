class SomeClass:
    def __init__(self):
        self.x = 1

    def increment_thing(self):
        self.x += 1
    
    def get_thing(self):
        return self.x

one = SomeClass()
two = SomeClass()

print(f"\nINi one: {one}")
print(f"\nIni two: {two}")
