# def count():
#     nums = input("Write your numbers: ")
#     odds = 0
#     evens = 0
#     for i in  nums:
#         if i % 2 == 0:
#             odds += 1
#         else:
#             evens += 1
#     print(odds)
#     print(evens)

# print(count())
def count(nums):
    
    odds = 0
    evens = 0
    for i in  nums:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    print(odds)
    print(evens)
    
#nums = input("Write your numbers: ")
count([1, 2, 3, 4, 5])