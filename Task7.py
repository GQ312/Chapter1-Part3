def count(nums):
    negative = []
    positive = []
    for i in nums:
        if int(i) > 0:
            positive.append(i)
        elif int(i) < 0:
            negative.append(i)
        else:
            continue
    print(f"Negative numbers: {negative}")
    print(f"Positive numbers: {positive}")

count_num = input("Write your numbers: ").split(" ")

count(count_num)