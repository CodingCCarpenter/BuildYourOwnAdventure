class Store:
    # must always pass in self
    def __init__(self, name, categories):
        # attributes
        self.name = name 
        self.categories = categories

    def __str__ (self):
        return f'{self.name} has {len (self.categories) } categories''

my_store = Store("Pets Plus", [])
print(my_store)