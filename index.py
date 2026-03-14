print("Hello, World!")

print("I'm learning Python")

print("we learn 5 concept + 1 OOP")

## variable +basic calculation
## data type
## data structure
## control flow
## function
## OOP

## 1. Variable + calculation

print(1+1)
print("four:",2+2)

print("normal division",3/2)
print(3/2.0)
print("floor division:",3//2)
print("modulo:",3%2)

print("ยกกำลัง:",3**2)

##naming varibable 
income = 1000
expense = 500
saving = income -expense
print("saving:",saving)

## remove variable 
del saving
# print(saving) # error because saving is deleted


## data type

#int จำนวนเต็ม
#float เลขทศนิยม
#string ข้อความ
#boolean  T & F

name = "Pure"
text = "I'm a man"
age = 27
gpa = 3.41
fav_lang = "typescript"
movie_lover = True
print(name,text,age, gpa , fav_lang, movie_lover)

print(type(name))

##type hint 
str_name: str = "Toy"
print(type(str_name))


##convert type
num1 =10 
str(num1)

int(True)
int(False)

## f-string
name = "Pure"
age =  27
lang = "typescript"
text = f"My name is {name}, I'm {age} years old and I love {lang}"

print(text)

## DATA STRUCTURE
## list ==== array
## tuble
## dictionary
## set

## shopping list
mom_list = ["egg", "milk", "bread"]

##check lenght of list
print("Length of mom_list:", len(mom_list))


print("mom_list:",mom_list)
## slice item in a list
print("momlist_slice:",mom_list[0:])
print("momlist_slice:",mom_list[0:2])

##function vs method
len(mom_list)
print(len(mom_list))

##list method
## function ที่สามารถใช้ได้กับ list เท่านั้น 
mom_list.append("carrot")

print("mom_list carrot:",mom_list)

## remove last item
mom_list.pop()
print("mom_list pop:",mom_list)

##insert item at the index we want
mom_list.insert(1,"Bababa")

print("mom_list Bababa:",mom_list)

##remove carrot
mom_list.remove("egg")

print("mom_list remove egg:",mom_list)

### string method
text = "I love you"
print(text.capitalize())


##mutable vs immutable

#mutable = can change/transform e.g. list dict
#immutable = cannot change/transform e.g. string tuple

##new variable 
language = "python"
print(language[-0])

##update item in mom list(mutable )
mom_list.append("orange juice")
mom_list[0]=("duck egg")

print("mom_list update:",mom_list)

text =text.replace("I","We")
print("new text:", text)


text = ".......hello......"
text = text.strip(".")
print("strip text:",text)


##split text into list 
text = "I love learning pythob"
split_text = text.split(" ")
print("split text:",split_text)
## " " =ข้อความทั้งหมด
" ".join(split_text)
print("join text:",split_text)


##tuple is immutable
my_tub =()
print(type(my_tub))

books = ("python 101", "python 102", "python 103")
# books[0] = "python 201" # error because tuple is immutable  

##TUPLE UNPACKING
x,y,z = (100,200,300)
print(x+y+z)

##dictionary: mutable //object in js
### key-value pair

movie = {
"title": "The Dark Knight",
"year": 2006,
"rating": {
"imdb": 8.6,
"rottentomatoes": 9.1
},
"cast": ["A", "B", "C"]
}
print("movie:",movie)

movie["title"] = "Superwoman"
movie["year"] = 2026

print("movie:",movie)

movie["revenue"] = 1000
del movie["revenue"]
print("movie with del:",movie)

##key items values
print("Keys:", movie.keys())
print("Values:", movie.values())
print("Items:", movie.items())

titles=list(movie.keys())

print("titles:",titles)

##update value in dict
movie["cast"][0] = "Christian Bale"
print("movie cast update:",movie)

##set mutable

##unique value in a set 
colors = ["red","blue","blue","red"]
set_colors = set(colors)
print("set_colors:",set_colors)

##set will delete duplicate value
books = {"book1","book2","book3","book1"}
print("books type:",type(books))

set_colors.add("yellow")
set_colors.add("salmond")

print("set_colors add:",set_colors)

set_colors.remove("salmond")

print("set_colors after removal:",set_colors)


##control flow 
## if 

score = 5
print("Program Start")
if score >=80:
    print("Passed")
elif score >=70:
    print("Almost Passed")
elif score >=60:
    print("Not Passed")
else:
    print("Totally Failed")
print("End of program")

##get input from user
name = input("what is your name?: ")
age = int(input("what is your age?: "))
print("Hello",name)
print("age:",age)
##multiple condition
has_it = True
age_over_18 = False
vip_customer = True
if has_it and (age_over_18 or vip_customer):
    print("Welcome to the club")
else:
    print("Sorry, you cannot enter the club")

## for & while loop
items = ["eggs","milk","bread"]
for item in items:
    if item == "milk":
        print("CP Meiji")
    else:
        print(item)
##list comprehension
result = [ ]
for item in items:
    result.append(item.upper())
print("result:",result)

[item.upper() for item in items]
print("resultasdasd:",result)

## while loop
while True:
    ##do something
    user_input = input("Type 'exit' to quit: ")
    if user_input.lower() == "exit":
        print("Exiting the program...")
        break
    else:
        print("This will run forever")

## function
## we use "def" to define a function
def greet(name):
    print(f"Hello, {name}!")

greet("Pure")

##new function cube()
def cube(base,power):
    return base**power

result = cube(2,3)
print("cube result:",result)

##function can return multiple value
## using tuple unpacking

def random_fun(base):
    return base**2, base**3,base**4

x,y,z = random_fun(5)
print(x,y,z, x+y+z)

##build my own chatbot
def chatbot():
    print("Welcome to the chatbot!")
    name = input("What is your name? ")
    print(f"Hello, {name}! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            print(f"Chatbot: You said '{user_input}'")

chatbot()

### OOP
### Object oriented programming
class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def working(self):
        print(f"{self.name} is working now")
employee1 = Employee("Pure","Software Engineer")
print("employee1 name:",employee1.name)
print("employee1 position:",employee1.position)
employee1.working()
print(type(employee1))