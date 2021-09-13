trips = int(input())
places = []
for i in range(trips):
    stops = int(input())
    unique_cities= []
    for i in range(stops):
        city = input()
        if city in unique_cities:
            pass
        else:
            unique_cities.append(city)
    places.append(len(unique_cities))
for i in places:
    print(i)
