import hashmap

#创建州名简称的map
states=hashmap.new()
hashmap.set(states,'Oregon','OR')
hashmap.set(states,'Florida','FL')
hashmap.set(states,'California','CA')
hashmap.set(states,'New York','NY')
hashmap.set(states,'Michigan','MI')

#州&其中城市
cities=hashmap.new()
hashmap.set(cities,'CA','San Francisico')
hashmap.set(cities,'MI','Detroit')
hashmap.set(cities,'FL','Jacksonville')

#添加一些城市
hashmap.set(cities,'NY','New York')
hashmap.set(cities,'OR','Portland')

#打印一些城市
print("-"*10)
print("NY state has: {}.".format(hashmap.get(cities,'NY')))
print("OR state has: {}.".format(hashmap.get(cities,'OR')))

#打印一些州简称
print("-"*10)
print("Michigan's abbreviation is: {}." .format(hashmap.get(states, 'Michigan')))
print("Florida's abbreviation is: {}.".format(hashmap.get(states,'Florida')))

#打印一些城市
print("-"*10)
print("Michigan has: {}.".format(hashmap.get(cities,hashmap.get(states,'Michigan'))))
print("Florida has: {}.".format(hashmap.get(cities,hashmap.get(states,'Florida'))))

#打印所有简称
print("-"*10)
hashmap.list(states)

#打印所有城市
print("-"*10)
hashmap.list(cities)

print("-"*10)
state=hashmap.get(states,'Texas')

if not state:
    print("Sorry, no Texas.")

city=hashmap.get(cities,'TX','Does not Exist.')
print("The city for the state 'TX' is: {}.".format(city))

print("-"*10)
bMap=hashmap.dump(aMap=states)
hashmap.list(bMap)