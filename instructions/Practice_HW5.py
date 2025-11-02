def mystery_function(x):
    x[1][0] = 100

x = (3, [1, 2, 3], [4, 5, 6])
print(x)

mystery_function(x)
print(x)