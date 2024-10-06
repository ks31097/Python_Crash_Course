favorite_places = {
    'name1': ['place1.1', 'place1.2', 'place1.3',],
    'name2': ['place2.1',],
    'name3': ['place3.1', 'place3.2',],
}

if favorite_places:
    for name, favorite_place in favorite_places.items():
        if len(favorite_place) == 1:
            print(f"\n{name.title()}'s favorite place is:")
        else:
            print(f"\n{name.title()}'s favorite places are:")
        
        for place in favorite_place:
            print(f"\t{place.title()}")
else:
    print('Nothing to show!')