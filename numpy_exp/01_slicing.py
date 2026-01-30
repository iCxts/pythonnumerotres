import numpy as np

a = np.arange(20).reshape(4, 5)
print("Original array (4x5):")
print(a)

print("\na[1, 2] - single element:")
print(a[1, 2])

print("\na[1] - entire row 1:")
print(a[1])

print("\na[:, 2] - entire column 2:")
print(a[:, 2])

print("\na[1:3] - rows 1 to 2:")
print(a[1:3])

print("\na[:, 1:4] - columns 1 to 3:")
print(a[:, 1:4])

print("\na[1:3, 2:5] - submatrix (rows 1-2, cols 2-4):")
print(a[1:3, 2:5])

print("\na[::2] - every other row:")
print(a[::2])

print("\na[:, ::2] - every other column:")
print(a[:, ::2])

print("\na[::-1] - rows reversed:")
print(a[::-1])

print("\na[:, ::-1] - columns reversed:")
print(a[:, ::-1])

b = np.arange(10)
print("\n1D array b:")
print(b)

print("\nb[2:7] - elements 2 to 6:")
print(b[2:7])

print("\nb[::3] - every third element:")
print(b[::3])

print("\nb[-3:] - last 3 elements:")
print(b[-3:])

c = a[:, 1:4]
print("\nSlice c = a[:, 1:4] (view, not copy):")
print(c)
c[0, 0] = 999
print("\nAfter c[0,0] = 999, original a is modified:")
print(a)

a[0, 1] = 1
print("\nReset a[0,1] = 1")
