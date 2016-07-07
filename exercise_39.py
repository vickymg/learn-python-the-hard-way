# Dictionaries, Oh Lovely Dictionaries

# Dict is like Ruby hash

# Compare lists...
things = ['a', 'b', 'c', 'd']
print things[1]
# => b
things[1] = 'z'
print things[1]
# => z
print things
# => ['a', 'z', 'c', 'd']

# ...with dicts
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print stuff['name']
# => Zed
print stuff['age']
# => 36
print stuff['height']
# => 74
stuff['city'] = "San Francisco"
print stuff['city']
# => San Francisco
stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[2]
# => Neato
print stuff
# => {'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 36, 'height': 74}

# to delete things...
del stuff['city']
del stuff[1]
del stuff[2]
print stuff
# => {'name': 'Zed', 'age': 36, 'height': 74}

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

separator = '-' * 10
# print out some cities
print separator
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

# print some states
print separator
print 'Michigan\'s abbreviation is: ', states['Michigan']
print 'Florida\'s abbreviation is: ', states['Florida']

# do it by using the state then cities dict
# gets abbrev from states, and then uses this to access cities
print separator
print 'Michigan has: ', cities[states['Michigan']]
print 'Florida has:', cities[states['Florida']]

# print every state abbreviation
print separator
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print separator
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print separator
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

# safely get an abbreviation by state that might not be there
print separator
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
