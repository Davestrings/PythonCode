fruits = {"orange": "a sweet, orange citrus fruit", "apple": "good for making cider",
          "lemon": "a sour, yellow citrus fruit", "grape": "a small, sweet fruit growing in bunches",
          "lime": "a sour, green citrus fruit", "pear": "an odd shaped apple"}
# print(fruits)
for i in fruits:
    print(fruits[i])

del fruits["pear"]
print(fruits)

# while True:
#     dict_key = input("please enter a search key: ")
#     if dict_key == "quit":
#         break
#     elif dict_key in fruits:
#         print(fruits[dict_key])
#     else:
#         print("{} is not available".format(dict_key))
# Alternatively, you can get dictionary value using the get method as below

# while True:
#     dict_key = input("please, enter a search key: ")
#     if dict_key == "quit":
#         break
#     description = fruits.get(dict_key, "{} not available.".format(dict_key))
#     print(description)

# dictionaries are unordered. To output an ordered form of a dictionary see below
# 1
ordered_keys = list(fruits.keys())
ordered_keys.sort()
for i in ordered_keys:
    print(i,":", fruits[i])
print("="*15)

# Alternatively, using the method sorted
ordered_key = sorted(list(fruits.keys()))
for i in ordered_key:
    print(i,":", fruits[i])

print("="*15)
print(fruits.items())
fruits_tuple = tuple(fruits.items()) # creates a tuple from a dictionary
print("="*15)
print(fruits_tuple)
for snack, description in fruits_tuple:
    print(snack, 'is', description)
