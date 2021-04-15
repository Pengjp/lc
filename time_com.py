# array = [1,2, 3, 4, 5,5, 6, 7, 8, 9, 10];
# search_digit = 10;
#
# def search(arr，key):
#     for i in arr: # O(N)
#         if i == key:
#             return True
#     return False
#
# def min(arr):
#     ans = []
#     for i in arr:
#         ans.append(i)
#     return ans

array = [None] * 2
array[0] = 100
print(array)
print(hex(id(array)))
print('--------------------')
array[1] = 100
print(array)
print(hex(id(array)))
print('--------------------')
array.append(10)
print(array)
print(hex(id(array)))
