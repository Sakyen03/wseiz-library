from person import Person

class Librarian(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
