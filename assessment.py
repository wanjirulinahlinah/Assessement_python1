# Q1
# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# Sudo code

# INPUT 
# title
# content
# length
# moral lessons
# target-age-group

# OUTPUT
# in class story i will have this methods
#  get_title
#  get_content
#  get_moral+lessons
#  get_target_age_group
# in class story teller i will have this methods
# get_name
# get_language
# get_culture
# tell_story
# in class translatei will have the method translate
# translate

# # proccess
# create a class for story and have attributes like 
# title, content, length, moral_lessons, target_age_group
# create a different class for: 
# storyteller with attributes like 
# name, language, culture
# and a class for translated_story

class story:
    def __init__(self,title,content,length,moral_lessons,target_age_group) :
        self.title = title
        self.content = content
        self.length= length
        self.moral_lessons=moral_lessons
        self.target_age_group=target_age_group


    def get_title(self):
        return self.title
    
    def get_length(self):
        return self.length
    
    def get_content(self):
        return self.content
    
    def get_moral_lessons(self):
        return self.title
    
    def get_targe_age_group(self):
        return self.title
    

    
  

class StoryTeller:
    def __init__(self,name,language,culture):
        self.name=name
        self.language=language
        self.culture=culture
  
    
    def get_name(self):
        return self.name
    
    def get_language(self):
        return self.language
    
    def get_culture(self):
        return self.culture
    
    def tell_story(self, story):
        print(f"Story Title: {story.get_title()}")
        print(f"Story Content: {story.get_content()}")
        print(f"Story Length: {story.get_length()}")
        print(f"Moral Lessons: {story.get_moral_lessons()}")
 
class Translator:
    def translate(self, story, target_language):
      

story = Story(
    title="Angels never die",
    content="Long time ago...",
    length=10,
    moral_lessons=["peace", "christianity"],
    target_age_group="youths"
)

storyteller = StoryTeller(
    name="Linah",
    language="English",
    culture="Kikuyu"
)



# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# SUDO CODE
# iNPUT
#  name
#  country
#  ingredients
#  preparation_time
#  cooking_method

# OUTPUT
# METHODS 
# def display

# PROCCESS
# TO HAVE A MAIN CLASS RECIPE AND THE SUBCLASSES FOR 
# `MoroccanRecipe`,
# # `EthiopianRecipe`, `NigerianRecipe`),
# THEN A METHOD DISPLAY INHERITING FROM the main class recipe




class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_method):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method

    def display(self):
        print("Recipe: {}".format(self.name))
        print("Country: {}".format(self.country))
        print("Preparation Time: {}".format(self.preparation_time))
     

    def calculate_nutrition(self):
          print("Recipe: {}".format(self.name)(self.country))


class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, spice_level):
        super().__init__(name, "kENYA", ingredients, preparation_time, cooking_method)
        self.spice_level = spice_level

    def display(self):
        super().display()
        print("Spice Level: {}".format(self.spice_level))


class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, injera_required):
        super().__init__(name, "", ingredients, preparation_time, cooking_method)
        self.injera_required = injera_required

    def display(self):
        super().display()
        print("retion Required: {}".format(self.retio_required))


class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, protein_source):
        super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method)
        self.vitamin_source = vitamin_source

    def display(self):
        super().display()
        print("Protein Source: {}".format(self.protein_source))










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
    def __init__(self, diet, lifespan):
        self.diet = diet
        self.lifespan = lifespan

    def eat(self):
        pass

    def reproduce(self):
        pass


class Predator(Species):
    def __init__(self, diet, lifespan, hunting_strategy):
        super().__init__(diet, lifespan)
        self.hunting_strategy = hunting_strategy

    def hunt(self):
        pass


class Prey(Species):
    def __init__(self, diet, lifespan, migration_pattern):
        super().__init__(diet, lifespan)
        self.migration_pattern = migration_pattern

    def flee(self):
        pass

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
    def __init__(self, name, country, musical_style, instruments):
        self.name = name
        self.country = country
        self.musical_style = musical_style
        self.instruments = instruments


class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time


class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.schedule = []

    def add_performance(self, performance):
        self.schedule.append(performance)



artist1 = Artist("Artist 1", "Country 1", "Style 1", ["Instrument 1"])
artist2 = Artist("Artist 2", "Country 2", "Style 2", ["Instrument 2"])

performance1 = Performance(artist1, "10:00 AM", "11:00 AM")

stage1 = Stage("Main Stage", 1000)
stage1.add_performance(performance1)





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
    
    


product1 = Product("pawpaw", 1.5, 10)
product2 = Product("Banana", 0.5, 20)
product3 = Product("Orange", 1.0, 15)


total_value1 = product1.calculate_total_value()
total_value2 = product2.calculate_total_value()


total_value_all = total_value1 + total_value2 + total_value3


print(f"Total value of {product1.name}: ${total_value1}")
print(f"Total value of {product2.name}: ${total_value2}")
print(f"Total value of {product3.name}: ${total_value3}")
print(f"Total value of all products: ${total_value_all}")

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
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_student_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)
    
    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60


student1 = Student("John Doe", 18, [80, 75, 90, 65, 70])

student1.display_student_info()


average_grade = student1.calculate_average_grade()

print("Average Grade:", average_grade)


if student1.has_passed():
    print("The student has passed.")
else:
    print("The student has not passed.")


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
            if flight.destination == destination and flight.date == date and flight.is_available():
                available_flights.append(flight)
        return available_flights


    def get_passenger_info(self, flight):
        return flight.passengers

    def generate_booking_confirmation(self, flight, passenger):
        if passenger in flight.passengers:
            confirmation = f"Booking confirmation for {passenger.name} on flight {flight.flight_number}."
            return confirmation
        return None


class Flight:
    def __init__(self, flight_number, destination, date, capacity):
        self.flight_number = flight_number
        self.destination = destination
        self.date = date
        self.capacity = capacity
        self.passengers = []

    def is_available(self):
        return len(self.passengers) < self.capacity

    def reserve_seat(self, passenger):
        if self.is_available():
            self.passengers.append(passenger)


class Passenger:
    def __init__(self, name):
        self.name = name



booking_system = FlightBooking()


flight1 = Flight("FL001", "UGANDA", "2023-06-20", 100)
flight2 = Flight("FL002", "London", "2023-06-22", 150)


booking_system.add_flight(flight1)
booking_system.add_flight(flight2)

available_flights = booking_system.search_flights("UGANDA", "2023-06-20")
print("Available flights:")
for flight in available_flights:
    print(f"Flight: {flight.flight_number}, Destination: {flight.destination}, Date: {flight.date}")

passenger1 = Passenger("John Smith")
if booking_system.reserve_seat(flight1, passenger1):
    print(f"Seat reserved for {passenger1.name} on flight {flight1.flight_number}")
else:
    print("Seat reservation failed. Flight is not available.")




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
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Copies available: {self.copies}"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies=1):
        new_book = Book(title, author, copies)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} has been added to the catalog.")

    def search_by_title(self, title):
        matching_books = [book for book in self.books if book.title.lower() == title.lower()]
        if matching_books:
            for book in matching_books:
                print(book)
        else:
            print(f"No books found with the title '{title}'.")

    def search_by_author(self, author):
        matching_books = [book for book in self.books if book.author.lower() == author.lower()]
        if matching_books:
            for book in matching_books:
                print(book)
        else:
            print(f"No books found by the author '{author}'.")

    def display_book_details(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("The library catalog is empty.")

















