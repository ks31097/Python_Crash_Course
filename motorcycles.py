motorcycles = ['honda', 'yamaha', 'suzuki', 'bmw']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('harley-davidson')
print(motorcycles)

motorcycles.insert(0, 'New motorcycle')
print(len(motorcycles))
print(motorcycles)

del motorcycles[0]
print(len(motorcycles))
print(motorcycles)

last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a \"{last_owned.title()}\".")

print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a \"{first_owned.title()}\".")

print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

too_expensive = 'bmw'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")