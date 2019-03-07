#Dictionaries or hashes (containers) keys: values

#create a mapping of state to abbreviation
#mistake in the book. Dicts have { not [
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

#creeate a basic set of statees and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print cities
divider = '-' * 10
print divider
print "NY State has: ", cities['NY'] #key NY, value New York
print "OR State has: ", cities['OR']

#print some states
print divider
print "Michigan has: ", cities[states['Michigan']] #states returns MI, which is a key for cities
print "Florida has: ", cities[states['Florida']]

#print all state abbreviations
print divider

for state, abbrev in states.items(): #items returns key, value pairs. State: California abbrev: CA
    print "%s is abbreviated %s" % (state, abbrev)

#print every city in state
print divider
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now do both at the same time
print divider
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev]) #California state is abbreviated CA and has city San Francisco

print divider
#safely get an abbreviation by stat that might not be there
state = states.get('Texas', None) #get accepts the key, returns the associated value

if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does not exist') #second value is optional, something
#return if the key doesn't exist
print "The city for the state 'TX'is: %s" % city
