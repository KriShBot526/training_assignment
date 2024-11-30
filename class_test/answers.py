import math
import sys

# Question 1: Define a class called Vehicle. Include attributes like make, model, and year. Add an initialization method to set these attributes.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        
        if not isinstance(year, int):
            try:
                year =int(year)
            except ValueError:
                print('ValueError: Invalid Input. Year should be numeric')
                sys.exit(1)
        
        self.year = year

# Question 2: Add a method called display_info to the Vehicle class that prints out the vehicle’s information in a nicely formatted string.

    def display_info(self):
        print(f"{self.model} is a product of {self.make} made in the year {self.year}")

# Question 3: Create a subclass of Vehicle called Car that includes additional attributes like doors and engine_type. Override the display_info method to include these new attributes.

class Car(Vehicle):
    def __init__(self, make, model, year, no_of_doors, engine_type):

        if not isinstance(no_of_doors, int):
            try:
                no_of_doors =int(no_of_doors)
            except ValueError:
                print('ValueError: Invalid Input. Number of doors should be numeric')
                sys.exit(1)

        self.no_of_doors = no_of_doors
        self.engine_type = engine_type

        super().__init__(make, model, year)

    def display_info(self):
        print(f"{self.model} is a product of {self.make} made in the year {self.year}. It has a {self.engine_type} Engine and has {self.no_of_doors} no_of_doors")

# Question 4: Write a method in the Car class to start_engine. This method should print a message that says the engine is starting, using the engine_type in the message.

    def start_engine(self):
        print(f"{self.engine_type} Engine is Starting...")

# Question 5: Implement a Bicycle subclass that inherits from Vehicle. Include additional attributes such as gear_count and bicycle_type.
class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count, bicycle_type):

        if not isinstance(gear_count, int):
            try:
                self.gear_count =int(gear_count)
            except ValueError:
                print('ValueError: Invalid Input. Gear Count should be numeric')
                sys.exit(1)

        self.bicycle_type = bicycle_type

        super().__init__(make, model, year)

# Question 6: Create a Python class Circle. Use the __init__ method to set the radius and a method to calculate the area (use pi value from the math module).

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            try:
                self.radius = float(radius)
            except ValueError:
                print('ValueError: Invalid Input. Radius should be numeric')
                sys.exit(1)
        else:
            self.radius = radius

    def calculate_area(self):
        area = math.pi*(self.radius)**2
        print(f"The area of the circle is {area:.2f}")

# Question 7: Define a class Rectangle with attributes length and width. Include methods to calculate the area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, (int, float)) and isinstance(width, (int, float)):
            try:
                self.length = float(length)
                self.width = float(width)
            except ValueError:
                print('ValueError: Invalid Input. Dimensions should be numeric')
                sys.exit(1)

    def calculate_area(self):
        print(f"The area of rectangle is {self.length*self.width}")

    def calculate_perimeter(self):
        print(f"The perimeter of rectangle is {2*(self.length + self.width)}")

# Question 8: Create a class Employee with properties name and employee_id. Include a method to print an email address, assuming it's employee_id@company.com.

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __str__(self):
        return f"{self.name}: {self.employee_id}@company.com"

# Question 9: Extend the Employee class with a subclass Manager that has an additional attribute department and a method to print department details.

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        self.department = department

        super().__init__(name, employee_id)

    def __str__(self):
        return f"{super().__str__()}, belongs to {self.department}"
    
# Question 10: Define a class ComplexNumber to represent complex numbers. Include methods to add and multiply two complex numbers.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary

        print(ComplexNumber(real_part, imaginary_part))

    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)

        print(ComplexNumber(real_part, imaginary_part))

    def __str__(self):
        return f"{self.real} + {self.imaginary}i" if self.imaginary>0 else f"{self.real} - {-self.imaginary}i"
    
# Question 11: Create a class Book with attributes title, author, and price. Add a method to apply a discount to the price and another to format the book details as a string.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.discounted_price = price

    def apply_discount(self, discount_percentage):
        if (0 <= discount_percentage <= 100):
            self.discounted_price -= self.price * (discount_percentage / 100)
        else:
            print("Error: Discount percentage should be in between 0 to 100.")

    def __str__(self):
        return f"The price of {self.title} written by {self.author} is {self.price}, but it is now available at {self.discounted_price}"
    
# Question 12: Implement a class Flight that can keep track of airline, flight number, and the list of passengers (use passenger names).

class Flight:
    def __init__(self, airline, flight_number):
        self.airline = airline
        self.flight_nummber = flight_number
        self.list_of_passengers = []

    # Question 13: Add methods to the Flight class to add a passenger to the flight and to remove a passenger by name.
    def add_passenger(self, passenger_name):
        if passenger_name not in self.list_of_passengers:
            self.list_of_passengers.append(passenger_name)
            print("Passenger added.")
        else:
            print(f"{passenger_name} is already on the list")

    def remove_passenger(self, passenger_name):
        if passenger_name in self.list_of_passengers:
            self.list_of_passengers.remove(passenger_name)
            print("Passenger removed.")
        else:
            print(f"{passenger_name} is not on the list")

    def list_passengers(self):
        if self.list_of_passengers:
            print(f"Passengers on flight - {self.flight_nummber}({self.airline}) is:")

            for i, passenger in enumerate(self.list_of_passengers):
                print(f"{i+1}. {passenger}")
        
        else:
            print(f"There are no passengers on flight - {self.flight_nummber}({self.airline}).")

    def __str__(self):
        return f"The flight {self.flight_nummber} belongs to {self.airline} airlines."
    
# Question 14: Create a class Animal with an attribute species. Add a method make_sound that prints a generic sound.
    
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("hmm...")

# Question 15: Subclass Animal with Dog and Cat classes. Override the make_sound method to print "Woof" for dogs and "Meow" for cats.

class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        print("Meow")

# Question 16: Develop a class Calculator with methods for basic operations: add, subtract, multiply, and divide. Handle division by zero gracefully.

class Calculator:
    '''
    Accepts list of numbers to operate on.
    '''

    def add(self, numbers):
        print(f"Result of addition is {sum(numbers)}")

    def subtract(self, numbers):
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        
        print(f"Result of subtraction is {result}")

    def multiply(self, numbers):
        result = numbers[0]
        for number in numbers[1:]:
            result *= number

        print(f"Result of multiplication is {result}")

    def division(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            try:
                result = result / num
            except:
                print("Error: Cannot be divided by 0!")
        print(result)

# Question 17: Create a class WeatherForecast that has a method to add a temperature reading and another method to get the average temperature.

class WeatherForecast:
    def __init__(self):
        self.temperature_list = []

    def add_temperature(self, temperature):
        if isinstance(temperature, (int, float)):
            self.temperature_list.append(temperature)
        else:
            for i in temperature:
                if isinstance(i, (int, float)):
                    self.temperature_list.append(i)

    def avg_temperature(self):
        if self.temperature_list:
            print(f"The average temprature is {sum(self.temperature_list) / len(self.temperature_list)}")

# Question 18: Define a Polygon class with methods to calculate perimeter and area. This class should be designed to be subclassed by specific polygon types like triangles and squares.

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)
    
    def area(self):
        pass

# Question 19: Implement a subclass of Polygon for Triangle. Use attributes for the sides and appropriate methods to compute area (using Heron's formula).

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        if (side1+side2<=side3) or (side1+side3<=side2) or (side3+side2<=side1):
            print('ValueError: Invalid Input. Radius should be numeric')
            sys.exit(1)
        
        super().__init__([side1, side2, side3])

    def area(self):
        a, b, c = self.sides
        s = self.perimeter()/2

        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print(f"Area of Triangle is {area}")

# Question 20: Write a Square subclass of Polygon with a method override for area calculation specific to squares.

class Square(Polygon):
    def __init__(self, side_len):
        if side_len <= 0:
            print('ValueError: Invalid Input. Radius should be numeric')
            sys.exit(1)

        super().__init__([side_len]*4)

    def area(self):
        print(f"Area of square is {self.sides[0]**2}")

# Question 21: Create a class Timer that can be used to time operations in Python. Use the time module for tracking start and end times.

import time

class Timer:
    def __init__(self):
        self.start_timer = None
        self.end_timer = None

    def start(self):
        self.start_timer = time.time()
        self.end_timer = None

    def stop(self):
        if self.start_timer is None:
            print("Timer was not started yet...")
            return
        
        self.end_timer = time.time()

    def elapsed(self):
        if self.start_timer is None:
            print("Timer was not started...")
            return

        if self.end_timer is None:
            print(f"Elapsed time is {time.time() - self.start_timer}")
        else:
            print(f"Elapsed time is {self.end_timer - self.start_timer}")

# Question 22: Design a Queue class using lists. Implement methods for enqueue, dequeue, and viewing the queue.

class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.max_size is not None and len(self.queue >= self.max_size):
            raise OverflowError("Maximum Capacity Reached")

        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is already empty")

        self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty, so cannot peek")

        self.queue[0]

    def size(self):
        return len(self.queue)

    def __str__(self):
        return f"Queue: {self.queue}"

    def isEmpty(self):
        return len(self.queue) == 0

# Question 23: Create a class Stack with methods for pushing, popping, and checking the size of the stack.

class Stack:
    def __init__(self, max_size):
        self.stk = []
        self.max_size = max_size

    def push(self, item):
        if self.max_size is not None and len(self.stk >= self.max_size):
            raise OverflowError("Maximum Capacity Reached")

        self.stk.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is already empty")

        self.stk.pop(0)

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty, so cannot peek")

        self.stk[0]

    def size(self):
        return len(self.stk)

    def __str__(self):
        return f"Stack: {self.stk}"

    def isEmpty(self):
        return len(self.stk) == 0

# Question 24: Develop a MusicPlayer class with methods to play, stop, and load music tracks (simulated with print statements).

class MusicPlayer:
    def __init__(self, tracks=[]):
        self.tracks = tracks
        self.is_playing = False
        self.now_playing = ''

    def play(self, track_name=None):
        if (self.tracks):

            if track_name is None:
                self.is_playing = True
                self.now_playing = self.tracks[0]
                print(f"Playing Track: {self.now_playing}")

            elif (track_name.lower() in [x.lower() for x in self.tracks]):
                
                if not self.is_playing or (self.now_playing.lower() != track_name.lower()):
                    self.is_playing = True
                    self.now_playing = track_name
                    print(f"Playing Track: {self.now_playing}")
                
                else:
                    print(f"{self.now_playing} is already playing")
            else:
                print(f"{track_name} is not present in the list")
        else:
            print("Tracks list is empty. Nothing can be played")

    def stop(self):
        if self.is_playing:
            print(f"Stopped Track: {self.now_playing}")
            self.is_playing = False
        else:
            print("No track is playing")

    def load(self, track):
        if isinstance(track, str):
            self.tracks.append(track)
        else:
            for i in track:
                self.tracks.append(i)
        
        print(f"{track} has been loaded")

# Question 25: Implement a Database class that simulates a simple database interaction with methods to connect, disconnect, and execute a query (simulated with print statements).

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def connect(self):
        if not self.connected:
            self.connected = True
            print(f"Connected to database: {self.dbname}")
        else:
            print(f"Already connected to {self.dbname}")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print(f"Disconnected from database: {self.dbname}")
        else:
            print(f"Error: No database is connected")

    def exec(self, query):
        if self.connected:
            print(f"Executing query...")
        else:
            print(f"Error: Database not connected")

