# Find value that occurs in odd number of elements
# A non-empty array A consisting of N integers is given. The array contains an odd number of elements,
# and each element of the array
# can be paired with another element that has the same value, except for one element that is left unpaired.
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
#  indexes 0 and 2 have value 9,
# indexes 1 and 3 have value 3,
# indexes 4 and 6 have value 9,
# index 5 has value 7 and is unpair
#Given a number, return true if its even or false if its odd

a = [9, 9, 3, 3, 9, 9, 7]

def unpaired_item(array):
  d = {}

  for item in a:
    if item not in d:
      d[item] = 1
    else:
      d[item] += 1

  print(d)

  for k, v in d.items():
    if v == 1:
      return k

print(unpaired_item(a))