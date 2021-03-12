pets = ["dog", "cat", "bird"]
otherpets = ("mouse", "bird", "rabbit")
people = ("mike", "will", "john")

index = 0

dog = pets[0]
print(dog)
cat = pets[1]
print(cat)

firstlist = [1,2,3]
firstlist.extend(4,5,6)

print(firstlist)

count = 0

for pet in pets:
    print(pet)
    print(count)
    count += 1 