def change(nums):
    changed_nums = []
    for i in nums:
        if int(i) > 0:
            changed_nums.append(1)
        elif int(i) < 0:
            changed_nums.append(-1)
        elif int(i) == 0:
            changed_nums.append(0)
        else:
            continue
    print(f"Changed numbers are {changed_nums}")


enter_nums = input("Write your numbers: ").split(" ")

change(enter_nums)
