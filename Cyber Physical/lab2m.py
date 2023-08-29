# What will be the output if you change the decrement to 15?
start = 30
end=0
decrement = 15
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