thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])
thistuple[1] = "blackcurrant"

# the value is still the same:
print(thistuple)

for x in thistuple:
  print(x)

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

print(thistuple)
