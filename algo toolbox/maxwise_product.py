# # initial method fast
# # n = int(input())

# # nums = input().split()


# # for i in range(n):
# #     l1 = [int(n) for n in nums]

# # max1 = max(l1)

# # l1.remove(max1)
# # max2 = max(l1)

# # print(max1*max2)

# # iteration method

# # n = int(input())

# # nums = input().split()

# # for i in range(n):
# #     l1 = [int(n) for n in nums]

# # p = 0

# # for i in range(n):
# #     for j in range(i+1,n):
# #         p = max(p,l1[i]*l1[j])

# # print(p)

# # new method

# n = int(input())

# nums = input().split()

# for i in range(n):
#     l1=[int(n) for n in nums]

# max_ind1 = -1
# for i in range(n):
#     if max_ind1 == -1  or l1[i] > l1[max_ind1]:
#         max_ind1 = i

# max_ind2 = -1
# for i in range(n):
#     if i != max_ind1 and (max_ind2 == -1 or l1[i] > l1[max_ind2]):
#         max_ind2 = i

# print(l1[max_ind1]*l1[max_ind2])


# # #Naive approach
# # def max_prod_naive(arr):
# #     product = 0
# #     for i in range(len(arr)):
# #         for j in range(i+1,len(arr)):
# #             product = max(product,arr[i]*arr[j])
# #     return product
# # #Fast approach
# # def max_prod_fast(arr):
# #     p1 = max(arr)
# #     arr.remove(p1)
# #     p2 = max(arr)
# #     return p1*p2

# # def max_prod_faster(arr):
# #     max_ind1 = -1
# #     for i in range(len(arr)):
# #         if max_ind1 == -1  or arr[i] > arr[max_ind1]:
# #             max_ind1 = i
# #     print(max_ind1)

# #     max_ind2 = -1
# #     for i in range(len(arr)):
# #         if i != max_ind1 and (max_ind2 == -1 or arr[i] > arr[max_ind2]):
# #             max_ind2 = i
                          
# #     return arr[max_ind1]*arr[max_ind2]

# # # #Stress test
# # # from random import randint
# # # def max_prod_stress(N,M):
# # #     while True:
# # #         n = randint(2,N)
# # #         print(n)
# # #         A = [None]*n
# # #         for i in range(n):
# # #             A[i] = randint(0,M)
# # #         print(A)
# # #         result1 = max_prod_naive(A)
# # #         result2 = max_prod_faster(A)
# # #         if result1==result2:
# # #             print('OK')
# # #         else:
# # #             print('Wrong answer:',result1,result2)
# # #             return
# # # max_prod_stress(2,100)


import sys

def max_pairwise_product(a):
    # Initialize the two largest numbers
    first_max = second_max = -sys.maxsize

    for number in a:
        if number > first_max:
            # Update both first and second max
            second_max = first_max
            first_max = number
        elif number > second_max:
            # Update only second max
            second_max = number

    return first_max * second_max

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))

    max_product = max_pairwise_product(a)
    print(max_product)

main()
