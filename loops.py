# fruits = ["apples", "oranges", "bananas"]

# for index in range(len(fruits)):
# #     print fruits[index]

# def sum_nums(num):
#     return_sum = 0
#     for item in range(num):
#         return_sum = return_sum + item
#     return return_sum

# print sum_nums(3)

def sum_nums2(num):
    if num < 0:
        neg_num = 0
        for item in range(num, 0):
            neg_num = neg_num + item
        return neg_num
    else:
        return_sum = 0
        for item in range(num):
            return_sum = return_sum + item
        return return_sum

print sum_nums2(-5)