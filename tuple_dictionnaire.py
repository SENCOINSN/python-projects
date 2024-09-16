tuple_1 = (1, 2, 4, 8)
tuple_2 = 1, .5, .25, .125
 
print(tuple_1)
print(tuple_2)

empty_tuple = ()


my_tuple  = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)



my_tuple =  (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3 # multiplier le tuple par 3 repeter trois fois le tuple

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_numbers['Suzy'])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for english, french in dictionary.items():  # return tuple
    print(english, "->", french)



dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
for french in dictionary.values():
    print(french)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary['swan'] = 'cygne'
print(dictionary)


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary.update({"duck": "canard"})
print(dictionary)
 

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
del dictionary['dog']
print(dictionary)

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
dictionary.popitem()
print(dictionary) # outputs: {'cat': 'chat', 'dog': 'chien'}

# school class dictionary example program

my_tuple_1 = 1,
print(type(my_tuple_1)) # outputs: <class 'tuple'>
 
my_tuple_2 = 1 # This is not a tuple.
print(type(my_tuple_2)) # outputs: <class 'int'>


my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(len(my_tuple)) # outputs: 5
print(my_tuple[3]) # outputs: [3, 4]


# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
 
# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
 
# Example 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)
# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
 
print(tuple_4)
print(tuple_5)


my_tuple = tuple((1, 2, "string"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # outputs: [2, 4, 6]
print(type(my_list)) # outputs: <class 'list'>
tup = tuple(my_list)
print(tup) # outputs: (2, 4, 6)
print(type(tup)) # outputs: <class 'tuple'>

tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # outputs: <class 'list'>

pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }
 
item_1 = pol_eng_dictionary["gleba"] # ex. 1
print(item_1) # outputs: soil
 
item_2 = pol_eng_dictionary.get("woda") # ex. 2
print(item_2) # outputs: water

pol_eng_dictionary = {"kwiat": "flower"}
 
pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower', 'gleba': 'soil'}
 
pol_eng_dictionary.popitem()
print(pol_eng_dictionary) # outputs: {'kwiat': 'flower'}

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
for item in pol_eng_dictionary:
    print(item)
 
#          woda
#          gleba


# via tuple

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value) 
    

# verifier si une cle est dans le dictionnaire

pol_eng_dictionary = {
    "zamek": "castle", 
    "woda": "water", 
    "gleba": "soil"
    }
 
print("woda" in pol_eng_dictionary) # outputs: True
print("woda" not in pol_eng_dictionary) # outputs: False

# remove element from dictionary

pol_eng_dictionary = {
    "zamek": "castle", 
    "woda": "water", 
    "gleba": "soil"
    }
 
pol_eng_dictionary.pop("woda")
print(pol_eng_dictionary) # outputs: {'zamek': 'castle', 'gleba': 'soil'}

# copy dictionary

pol_eng_dictionary = {
    "zamek": "castle", 
    "woda": "water", 
    "gleba": "soil"
    }
 
pol_eng_dictionary_copy = pol_eng_dictionary.copy()
print(pol_eng_dictionary_copy) # outputs: {'zamek': 'castle', 'woda': 'water', 'gleba': 'soil'}

tup = 1, 2, 3
a, b, c = tup

print(a, b, c)
 
print(a * b * c)

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
 
print(duplicates) # outputs: 4


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    d3.update(item)
 
print(d3)

my_list = ["car", "Ford", "flower", "Tulip"]
 
t = tuple(my_list)
print(t)

# convert tuple to dictionary
t = (('a', 1), ('b', 2), ('c', 3))
 
d = dict(t)
print(d)

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(my_dictionary)
 
print(copy_my_dictionary)