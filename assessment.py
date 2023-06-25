# Q1
# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.






class Story:
   def __init__(self, title, length, moralLesson, ageGroup):
       self.title = title
       self.length = length
       self.moralLesson = moralLesson
       self.ageGroup = ageGroup


   def displayDetails(self):
       print(f"Title: {self.title}")
       print(f"Length: {self.length}")
       print(f"Moral Lesson: {self.moralLesson}")
       print(f"Age Group: {self.ageGroup}")


   def tellStory(self, storyTeller):
       print(f"{storyTeller.name} is telling a story in {storyTeller.language}:")
       self.displayDetails()




class Translator(Story):
   def __init__(self, title, length, moralLesson, ageGroup, name, language, targetLanguage):
       super().__init__(title, length, moralLesson, ageGroup)
       self.name = name
       self.language = language
       self.targetLanguage = targetLanguage


   def translateAndTell(self):
       print(f"{self.name} is translating and telling a story in {self.targetLanguage}:")
       translatedStory = Story(self.title, self.length, self.moralLesson, self.ageGroup)
       print("Translated Story:")
       translatedStory.displayDetails()


story1 = Story("The Lion and the Mouse", "Short", "Helping others is important", "Children")
story2 = Story("The Tortoise and the Hare", "Medium", "Slow and steady wins the race", "Children")


translator1 = Translator("The Lion and the Mouse", "Short", "Helping others is important", "Children", "Emma", "English", "French")
translator2 = Translator("The Tortoise and the Hare", "Medium", "Slow and steady wins the race", "Children", "Luis", "Spanish", "English")


translator1.translateAndTell()
translator2.translateAndTell()




# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.





class Recipe:
   def __init__(self, ingredients, preparation_time, nutritional_information):
       self.ingredients = ingredients
       self.preparation_time = preparation_time
       self.nutritional_information = nutritional_information


   def display_recipe(self):
       print("Ingredients", self.ingredients)
       print("Preparation Time", self.preparation_time)
       print("Nutritional Information", self.nutritional_information)


   def cooking_method(self):
       print("Add four glasses of water")
       print("Leave it to boil")
       print("Add two spoons of salt")
       print("Add three spoons of cooking oil")
       print("Add half a kilo of rice")
       print("Cover to simmer")




class MoroccanRecipe(Recipe):


   def display_recipe(self):


       super().display_recipe()


# It allows the subclass to inherit and execute the parent class's implementation of the method before adding 
# its own additional code.



   def cooking_method(self):


       print("On a pre-heated pan, add two spoons of cooking oil")


       print("Add two well-sliced onions")


       print("Add five well-chopped tomatoes")


       print("Leave the tomatoes to get heated and create a paste")


       print("Add boiled rice")










class NigerianRecipe(Recipe):


   def display_recipe(self):


       super().display_recipe()






   def cooking_method(self):


       print("On a pre-heated pan, add two spoons of cooking oil")


       print("Leave it to boil")


       print("Add five well-chopped tomatoes")


       print("Leave the tomatoes to get heated and create a paste")


       print("Add boiled rice")
       
       
       
       # Example usage
moroccan_recipe = MoroccanRecipe(
    ingredients=["Cooking oil", "Onions", "Tomatoes", "Rice"],
    preparation_time=15,
    nutritional_information="...",
)
moroccan_recipe.display_recipe()
moroccan_recipe.cooking_method()

nigerian_recipe = NigerianRecipe(
    ingredients=["Cooking oil", "Onions", "Tomatoes", "Rice", "Spices"],
    preparation_time=20,
    nutritional_information="...",
)
nigerian_recipe.display_recipe()
nigerian_recipe.cooking_method()










# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.
# sudo code 
# input
#  diet, typical lifespan, migration
# # patterns
# output
# different methods for different classes like
# def eat
# def produce
# def hunt
# def flee
# proccess
# create class species
# attrributes like diet,lifespan,hunting_strategy
# have other classes like predator with attributes
#  diet, typical lifespan, migration
# and a class prey
# with attributes
# diet, lifespan, migration_pattern



class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan

    def __str__(self):
        return self.name


class Predator(Species):
    def __init__(self, name, diet, lifespan, hunting_method):
        super().__init__(name, diet, lifespan)
        self.hunting_method = hunting_method

    def __str__(self):
        return f"{self.name} (Predator)"


class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern):
        super().__init__(name, diet, lifespan)
        self.migration_pattern = migration_pattern

    def __str__(self):
        return f"{self.name} (Prey)"


# Example usage:
lion = Predator("Lion", "Carnivore", 10, "Ambush hunting")
zebra = Prey("Zebra", "Herbivore", 20, "Seasonal migration")

print(lion)
print(zebra)


# Q4

# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.
# sudo code
# Input
# name, 
# country, 
# musical_style, 
# instruments
# output
# method add perfomance
# process
# class artist with attributes
# attributes
# name, 
# country, 
# musical_style, 
# instruments
# output
# method add perfomance
# other subclassess for perfomance and stage

class Artist:
    def __init__(self, name, country, musical_style):
        self.name = name
        self.country = country
        self.musical_style = musical_style

    def __str__(self):
        return self.name


class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.artist} ({self.start_time}-{self.end_time})"


class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.schedule = []

    def add_performance(self, performance):
        self.schedule.append(performance)

    def __str__(self):
        return self.name


# Example usage:
artist1 = Artist("Femi Kuti", "Nigeria", "Afrobeat")
artist2 = Artist("Salif Keita", "Mali", "Mande music")

performance1 = Performance(artist1, "18:00", "20:00")
performance2 = Performance(artist2, "20:30", "22:30")

stage1 = Stage("Main Stage", 1000)
stage1.add_performance(performance1)
stage1.add_performance(performance2)

print(stage1)
for performance in stage1.schedule:
    print(performance)






# 5. Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

# sodo code
# input
#  name, 
#  price, 
#  quantity
# output
# Implement a method to calculate the total value of the product (price * quantity).
# proccess
# class product
# attributes
# Name
# price
# quantity

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity


# Example usage:
product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)
product3 = Product("Headphones", 50, 20)

total_value1 = product1.calculate_total_value()
total_value2 = product2.calculate_total_value()
total_value3 = product3.calculate_total_value()

print(f"Total value of {product1.name}: {total_value1}")
print(f"Total value of {product2.name}: {total_value2}")
print(f"Total value of {product3.name}: {total_value3}")



# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.


# Sudo Code

input
#  name, age, grades
# output
# method
# calculate_average_grade
#  display_student_info
#  display_student_info
# proccess
# create class student with atrributes
#  name, age, grades
# and then the following methods
# calculate_average_grade
#  display_student_info
#  display_student_info


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60


# Example usage:
student1 = Student("John", 20, [80, 75, 90, 65, 70])
student2 = Student("Jane", 22, [55, 60, 45, 70, 80])

student1.display_student_info()
average_grade1 = student1.calculate_average_grade()
print(f"Average Grade: {average_grade1}")
print(f"Has Passed: {student1.has_passed()}")

print()

student2.display_student_info()
average_grade2 = student2.calculate_average_grade()
print(f"Average Grade: {average_grade2}")
print(f"Has Passed: {student2.has_passed()}")




# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

# sudo code
# input
# # flights
# output
# add_flight
# search_flights
#  manage passenger information, and generate booking
# confirmations.
# process
# class flightBooking
# with the following methods
# # flights
# output
# add_flight
# search_flights
#  manage passenger information, and generate booking
# confirmations.

class FlightBooking:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date and flight.has_available_seats():
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, flight, passenger_name):
        if flight.has_available_seats():
            flight.reserve_seat(passenger_name)
            return True
        else:
            return False

    def update_passenger_info(self, flight, passenger_name, new_info):
        flight.update_passenger_info(passenger_name, new_info)

    def generate_booking_confirmation(self, flight, passenger_name):
        return flight.generate_booking_confirmation(passenger_name)


class Flight:
    def __init__(self, flight_number, destination, date, total_seats):
        self.flight_number = flight_number
        self.destination = destination
        self.date = date
        self.total_seats = total_seats
        self.passengers = {}

    def has_available_seats(self):
        return len(self.passengers) < self.total_seats

    def reserve_seat(self, passenger_name):
        self.passengers[passenger_name] = {}

    def update_passenger_info(self, passenger_name, new_info):
        if passenger_name in self.passengers:
            self.passengers[passenger_name] = new_info

    def generate_booking_confirmation(self, passenger_name):
        if passenger_name in self.passengers:
            confirmation = f"Booking Confirmation\nFlight: {self.flight_number}\n" \
                           f"Destination: {self.destination}\n" \
                           f"Date: {self.date}\n" \
                           f"Passenger: {passenger_name}\n"
            return confirmation
        else:
            return "Passenger not found in the flight."


# Example usage:
booking_system = FlightBooking()

flight1 = Flight("FL001", "New York", "2023-07-01", 100)
flight2 = Flight("FL002", "London", "2023-07-02", 150)

booking_system.add_flight(flight1)
booking_system.add_flight(flight2)

available_flights = booking_system.search_flights("New York", "2023-07-01")
if available_flights:
    selected_flight = available_flights[0]
    passenger_name = "John Smith"

    if booking_system.reserve_seat(selected_flight, passenger_name):
        print("Seat reserved successfully.")
    else:
        print("No available seats on the selected flight.")

    booking_system.update_passenger_info(selected_flight, passenger_name, {"Seat Number": "A12"})

    confirmation = booking_system.generate_booking_confirmation(selected_flight, passenger_name)
    print(confirmation)
else:
    print("No available flights on the selected date and destination.") 





# Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.
# sudo code
# input
# title 
# authors
# copies
# output
# methods like
# add_book
# search_by_title
# def search_by_author
# def display_book_details
# process
# create a class  Book wih attributes wand  methods
# create a class  library catalog with  attributes andmethods

    
class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        return self.available_copies > 0

    def borrow_book(self):
        if self.is_available():
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        return found_books

    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        return found_books

    def display_book_details(self, book):
        print("Title:", book.title)
        print("Author:", book.author)
        print("Total Copies:", book.total_copies)
        print("Available Copies:", book.available_copies)


# Example usage:
catalog = LibraryCatalog()

book1 = Book("Python Crash Course", "Eric Matthes", 5)
book2 = Book("Deep Learning", "Ian Goodfellow", 3)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10)

catalog.add_book(book1)
catalog.add_book(book2)
catalog.add_book(book3)

searched_books = catalog.search_by_title("python crash course")
if searched_books:
    selected_book = searched_books[0]
    catalog.display_book_details(selected_book)
    if selected_book.is_available():
        selected_book.borrow_book()
        print("Book borrowed successfully.")
    else:
        print("Book is not available.")
else:
    print("Book not found in the catalog.")

print()

searched_books = catalog.search_by_author("F. Scott Fitzgerald")
if searched_books:
    selected_book = searched_books[0]
    catalog.display_book_details(selected_book)
    selected_book.return_book()
    print("Book returned successfully.")
else:
    print("Book not found in the catalog.")
