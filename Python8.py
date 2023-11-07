def greet_user():
    """Display a simple greeting."""  #docstring
    print("Hello!")

greet_user()

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")

def make_shirt(shirt_size, shirt_message):
    """Display information a shirt"""
    print("\nI want a " + shirt_size + ".")
    print("I want a " + shirt_size + " to say " + shirt_message +".")

make_shirt("SM", "I love you")
make_shirt("M", "Mad love")
make_shirt("Lg", "Self love")  #pg141

#Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name= first_name + " "+last_name
    return full_name.title()
musician = get_formatted_name("jimi", "hendrix")
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name= first_name + " "+ middle_name +" " + last_name
    return full_name.title()
musician = get_formatted_name("john", "lee", "hooker")
print(musician)

#make the middle name an optional argument
def get_formatted_name(first_name, last_name, middle_name=" "):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name= first_name + " "+ middle_name +" " + last_name
    else:
        full_name= first_name + " "+ last_name 
    return full_name.title()
musician = get_formatted_name("jimi", "hendrix")
musician = get_formatted_name("john", "lee", "hooker")
print(musician)

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first":first_name, "last": last_name}
    return person 
musician = build_person ("jimi", "hendrix")
print(musician)
