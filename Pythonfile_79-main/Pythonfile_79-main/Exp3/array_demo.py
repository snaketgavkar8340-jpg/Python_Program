from array import array

numbers = array('i', [10, 20, 30, 40, 50])

print("Array:", numbers.tolist())
numbers.append(60)
print("After adding:", numbers.tolist())
numbers.remove(20)
print("After removing:", numbers.tolist())
print("First element:", numbers[0])