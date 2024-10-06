from random import randint as rand

toppings = ['bread', 'meat', 'cheese', 'salad', 'vegetables', 'sauce', 'spread']

def make_sandwich(*sandwich):
    # for sandwich_component in sandwich:
    #     print(sandwich_component)
    print("The sandwich consists of:")
    for _ in sandwich:
        print('-' + ' ' + _)

def rand_numb(rand = rand):
    return rand(0, 6)

def components(toppings):
    return toppings[rand_numb()]

def quantity_of_components():
    counter = rand_numb()
    print(f"Counter: {counter}\n")
    
    while True:
        if counter == 0:
            break
        else:
            print(f"\ncounter")
           
            make_sandwich(components(toppings))
        counter -= 1   

quantity_of_components()