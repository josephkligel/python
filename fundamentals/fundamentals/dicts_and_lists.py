# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students[0])

sports_directory["soccer"][0] = "Andres"
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z)

# 2. Iterate through List and Dicts
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list_dict):
    list_string = []
    dash = " - "
    comma = ","

    for dictionary in list_dict:
        list_string = []
        for k, v in dictionary.items():
            list_string.append(f'{k} - {v}')
        print(', '.join(list_string))


iterateDictionary(students)

# 3. Get Values from a List of Dictionaries
def iterateDictionary2(key, some_list):
    for dictionary in some_list:
        print(dictionary[key])

iterateDictionary2('last_name', students)

# 4. Iterate through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k, v in some_dict.items():
        print('-' * 10)
        print(f'{len(v)} {k.upper()}')
        for item in v:
            print(item)

printInfo(dojo)