# LOGICAL ERROR 1
numbers = [10, 5, 3]
total = sum(numbers)
count = 2 # Should be len(numbers)

average  = total / count
print(f"Average is: {average}")

# LOGICAL ERROR 2
for i in range(1, 5):
    print(i)