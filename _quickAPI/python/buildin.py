""" zip """
a = [3, 2, 1]
b = [4, 5, 6, 7]
x = list(zip(a, b))  # exclude `7`
x2 = tuple(zip(a, b))
print(x)
print(x2)
# sort
sorted(x, key=lambda x: x[1], reverse=True)
print(x)

""" sorted """
array = list({"age": 20, "name": "a"}, {"age": 25,
             "name": "b"}, {"age": 10, "name": "c"})
array = sorted(array, key=lambda x: x["age"])
