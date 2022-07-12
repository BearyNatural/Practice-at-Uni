for a in range(1, 1000):

     for b in range(a, 1000):

         c = 1000 - a - b    # Find c by substracting a and b from 1000

         if a < b < c:       # Each number must be smaller than the next

             if c*c == a*a + b*b:   # Check if numbers are pythagorean triplet

                 product = a*b*c

                 print (f"The triplet numbers are: a: {a} + b: {b} + c: {c} = {product}")  # Calculate the product