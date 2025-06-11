L = ["Ram", 1, "Shyam", 2, "Aman", 3]

print("Original list:", L)

numbers = [x for x in L if isinstance(x, int)]
strings = [x for x in L if isinstance(x, str)]

numbers.sort()
strings.sort()

sorted_list = numbers + strings

print("Sorted list:", sorted_list)
