# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for x in range(0, 1000):
    for y in range(0, 1000):
        for z in range(0, 1000):
            if (x < y < z) & (x + y + z == 1000):
                # print(f"{x} + {y} + {z}")
                if (x**2 + y**2 == z**2):
                    print(f"{x}+{y}+{z}")
                    a = x 
                    b = y
                    c = z

# test
                    product = a * b * c
                    print(product)
                    sum = a + b + c
                    print(sum)
