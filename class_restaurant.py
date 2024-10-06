class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + ', ' + self.cuisine_type)

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open")

    def guests_served(self):
        print(self.number_served)

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served += number
        else:
            print("Something wrong!")

    def increment_number(self, new_guests):
        self.number_served += new_guests

# restaurant = Restaurant("name", "type")
# print(restaurant.name.capitalize())
# print(restaurant.cuisine_type.capitalize())
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.guests_served()
# restaurant.set_number_served(10)
# restaurant.guests_served()
# restaurant.increment_number(100)
# restaurant.guests_served()
# # print(f"Served: {restaurant.number_served}")
# # restaurant.number_served = 5
# # print(f"Served: {restaurant.number_served}")


# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine_type, *flavours):
#         super().__init__(name, cuisine_type)
#         self.flavours = flavours

#     def show_flavours(self):
#         for _ in self.flavours:
#             print(_)
    
# ice_cream_cafe = IceCreamStand(1, 2, 3, 4, 5)
# print(ice_cream_cafe.flavours)
# ice_cream_cafe.show_flavours()