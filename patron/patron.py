from person import Person

class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name)
        self.patron_id = patron_id
