class Automobile:
    """
    A class to represent an automobile.

    Attributes:
    ----------
    make : str
        The manufacturer of the automobile.
    model : str
        The model of the automobile.
    year : int
        The year the automobile was manufactured.
    mileage : int
        The mileage of the automobile.
    color : str
        The color of the automobile.
    """

    def __init__(self, make: str, model: str, year: int, mileage: int, color: int):
        """
        Constructs all the necessary attributes for the automobile object.

        Parameters:
        ----------
        make : str
            The manufacturer of the automobile.
        model : str
            The model of the automobile.
        year : int
            The year the automobile was manufactured.
        mileage : int
            The mileage of the automobile.
        color : str
            The color of the automobile.
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color

    def set_engine_size(self, engine_size: float):
        """
        Sets the engine size of the automobile.

        Parameters:
        ----------
        engine_size : float
            The size of the engine in liters.
        """
        self.engine_size = engine_size

    def set_fuel_type(self, fuel_type: str):
        """
        Sets the fuel type of the automobile.

        Parameters:
        ----------
        fuel_type : str
            The type of fuel the automobile uses (e.g., 'Petrol', 'Diesel', 'Electric').
        """
        self.fuel_type = fuel_type

    def set_transmission_type(self, transmission_type: str):
        """
        Sets the transmission type of the automobile.

        Parameters:
        ----------
        transmission_type : str
            The type of transmission the automobile uses (e.g., 'Manual', 'Automatic').
        """
        self.transmission_type = transmission_type

    def set_capacity(self, capacity: int):
        """
        Sets the seating capacity of the automobile.

        Parameters:
        ----------
        capacity : int
            The number of seats in the automobile.
        """
        self.capacity = capacity


class Student:
    student_count = 0

    def __init__(self, name, age, major):
        self.name =  name
        self.age = age
        self.major = major
        Student.student_count += 1 

student_a = Student('Jalla', '17','CS')
student_b = Student('Jake', '90','BS')        

print(student_a.__class__.student_count)
