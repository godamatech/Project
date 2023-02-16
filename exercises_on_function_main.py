#Python Crash Course
import greetings
from greetings import greeting_users
from greetings import greeting_users as gu
import greetings as g
from greetings import *

print("===    display_message() function    ===")
def display_message():
	return "Hello! I am learning fuction in python from the book 'Python Crash Course' "

print(display_message())
print()
	
print("===    favorite_book() function    ===")
def favorite_book(book_title):
	return f"One of my favorite books is {book_title.title()}."
	
print(favorite_book('Python Crash Course'))
print()

print("=====    make_shirt() function	=====")
def make_shirt(size, msg):
	return f"The size of your shirt is {size} and the message printed on it is {msg}."

print(make_shirt("medium", "Godama~Tech"))
print()
print(make_shirt(msg='Techie', size='large'))
print()

print("===    Modified make_shirt() function    ===")
def make_shirt(size="Large", msg="I love python"):
	return f"The size of your shirt is {size} and the message printed on it is {msg}."

print(make_shirt())
print()
print(make_shirt("medium"))
print()
print(make_shirt("x-large", "Big~Boss"))
print()


print("===    describe_city() function    ===")
def describe_city(ct_name="kano", country="Nigeria"):
	return f"{ct_name} is in {country}"
	
print(describe_city("Zaria"))
print()
print(describe_city("kaduna"))
print()
print(describe_city("Zindr", "Niger"))
print()

print("===    person() function    ===")
def person(f_name, l_name, m_name=''):
	if m_name:
		full_name=f"{f_name} {m_name} {l_name}"
	else:
		full_name=f"{f_name} {l_name}"
	return full_name

print(person('A','Bello', 'M'))
print(person('A', 'Bello'))
print()

print("===    build_person() function    ===")
def build_person(f_name, l_name, age=None):
	if age:
		person = {"first":f_name, "last":l_name, "age":age}
	else:
		person = {"first":f_name, "last":l_name}
	return person
print(build_person('Abdullah', 'Muhammad'))
print(build_person('Hassan', 'Muhammad', 20))
print()

print("===    get_formatted_name() function    ===")
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()
	
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First Name: ") 
	if f_name.lower() == 'q':
		break

	l_name = input("Last Name: ") 
	print()
	if l_name.lower() == 'q':
		break
	else: 		
		print(f"Hello {get_formatted_name(f_name, l_name).title()}!")

print()

print("===    city_country() function    ===")
def city_country(ct_name="kano", country="Nigeria"):
	return f"\"{ct_name}, {country}\""
print(city_country())
print(city_country("Santiago", "Chile"))
print(city_country("Accra", "Ghana"))

print()
print("===    make_album() function    ===")
def make_album(artist_name, album_title):
	d = {"Artist":artist_name, "Album":album_title}
	return d
print(make_album("Daniel", "ABC"))
print(make_album("Davido", "XYZ"))
print(make_album("Wizkid", "PQR"))
print()

# print("===    greeting_users() function    ===")
# def greeting_users(names):
# 	 for name in names:
# 		 print(f"Hello {name.title()}!")

# usernames = ["Abdullahi", "Tijjani", "Mahmud", "Ishaq"]
# greeting_users(usernames)
# print()

print("===    Modifying a List    ===")
unprinted_designs  = ['phone case', 'robot pendant', 'dodecahedron']
completed_models  = []
while unprinted_designs:
	current_model  = unprinted_designs.pop()
	print(f"Printing Model: {current_model}")
	completed_models.append(current_model)

print(f"\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

print()

print("=== methods for modifying List and displaying completed models ===")
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_model  = unprinted_designs.pop()
		print(f"Printing Model: {current_model}")
		completed_models.append(current_model)


def show_completed_models(completed_models):
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
print()
show_completed_models(completed_models)

print()
print("=== Preventing a Function from Modifying a List ===")
print_models(unprinted_designs[:], completed_models)
print()
show_completed_models(completed_models)



print()
print("=== show_messages() ===")
def show_messages(msg_list):
	for msg in msg_list:
		print(msg)

msgs = ["Assalamualaikum", "Good Morning!", "How are you doing?", "How was your family?"]
show_messages(msgs)

print()
print("=== send_messages() ===")
sent_messages = []
def send_messages(msg_list):
	while msg_list:
		current_msg = msg_list.pop()
		print(current_msg)
		sent_messages.append(current_msg)

msgs = ["Assalamualaikum", "Good Morning!", "How are you doing?", "How was your family?"]
send_messages(msgs)
print()
print("The messages After calling the function")
print(f"Initial Messages: {msgs}")
print(f"Sent Messages: {sent_messages}")
print(f"The initial list after calling function: {msgs}")

print()
print("=== Archived Messages ===")
msgs = ["Assalamualaikum", "Good Morning!", "How are you doing?", "How was your family?"]
send_messages(msgs[:])
print()
print(f"The initial list after calling function: {msgs}")

print()
print("=== Sandwiches ===")
def make_sandwiche(*items):
	print("Making Sandwiche with the following items:")
	for item in items:
		print(f"- {item}")

make_sandwiche("Vanilla", "Chocolate")
make_sandwiche("Milk", "Chocolate", "Sugar")
make_sandwiche("Butter")

print()
print("=== User Profile ===")
def build_profile(f_name, l_name, **user_info):
	user_info["first"] = f_name 	
	user_info["last"] = l_name
	return user_info

user_profile=build_profile("Abdullahi", "Bello", origin="Kano", hobbies=['Personnal Research', 'Athletics', 'Football'], languages=['Hausa','Arabic','English'])
print(user_profile)

print()
print("=== Cars ===")
def make_car(manufacturer, model, **car_info):
	car_info['manufacturer'] = manufacturer 
	car_info['model'] = model 
	return car_info
	
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
print()

print("===    Importing greeting_users() function from greeting    ===")
names = ["Abdullahi", "Tijjani", "Mahmud", "Ishaq","Zaharaddeen"]
g.greeting_users(names)
print()