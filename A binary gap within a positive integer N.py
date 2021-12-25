# Initialize array
A = [3, 8, 9, 7, 6];
# K determine the number of times an array should be rotated
K = 3;

# Displays original array
print("Original array: ");
for i in range(0, len(A)):
    print(A[i]),

# Rotate the given array by n times toward left
for i in range(0, K):
    # Stores the first element of the array
    first = A[0];

    for j in range(0, len(A) - 1):
        # Shift element of array by one
        A[j] = A[j + 1];

        # First element of array will be added to the end
    A[len(A) - 1] = first;

print();

# Displays resulting array after rotation
print("Array after left rotation: ");
for i in range(0, len(A)):
    print(A[i]),