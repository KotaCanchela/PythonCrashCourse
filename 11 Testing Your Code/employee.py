class Employee:
    """Takes in and stores attributes for an employee."""

    def __init__(self, first, last, salary=0):
        """Initializes attributes for an employee"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase

    def show_attributes(self):
        print(
            f"The employee is {self.first.title()} {self.last.title()} and has a salary of {self.salary}"
        )


my_employee = Employee("Dakota", "canchela", salary=1000)
my_employee.show_attributes()

my_employee.give_raise()

my_employee.show_attributes()

my_employee.give_raise(6000)

my_employee.show_attributes()