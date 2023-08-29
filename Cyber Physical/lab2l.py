# Write a program where
start = 30
end=0
decrement = 3
# Continue the loop if start number becomes 17  **see below**

while start >= end:
    print(start)
    
    if start == 17:
        print("Skipping special action for 17!")
        start -= decrement
        continue
        
    start -= decrement

# test:

# print()