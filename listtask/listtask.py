# Question 01

# Write a program that removes duplicates from a list of numbers while preserving the order without set()

# numList = [1, 2, 3, 2, 4, 5, 1, 6]
# uniqueList = []
# for num in numList:
#     if numList.count(num) > 1:
#         numList.remove(num)
# numList.sort()        
# print(numList)     
# for num in numList:
#     if num not in  uniqueList:
#         uniqueList.append(num)
# print(uniqueList)        

# Question 02
#Write a program to find the second largest number in a list without sorting it.

# numList = [1, 2, 3, 2, 4, 7, 5,10, 1, 6, 8]

# maxNum = float('-inf')  # Initialize max as the smallest possible value
# secondLarge = float('-inf')  # Initialize second max
# print(maxNum)
# print(secondLarge)
# for num in numList:
#     if num > maxNum:
#         secondLarge = maxNum  # Update second largest before changing max
#         maxNum = num  # Update maxNum
#     elif num > secondLarge and num < maxNum:
#          secondLarge = num  # Update second largest only if it's smaller than maxNum

# print("Largest Number:", maxNum)
# print("Second Largest Number:", secondLarge)

# Question 03

# Write a program that takes two sorted lists and merges them into one sorted list.

# listOne = [1, 3, 5, 7]
# listTwo = [2, 4, 6, 8]
# sortedList = []

# i, j = 0, 0

# while i < len(listOne) and j < len(listTwo):
#     if listOne[i] < listTwo[j]:
#         sortedList.append(listOne[i])
#         i += 1
#     else:
#         sortedList.append(listTwo[j])
#         j += 1

# # Add remaining elements from either list
# sortedList.extend(listOne[i:])
# sortedList.extend(listTwo[j:])

# print(sortedList)

# Question 04

# Write a program that finds all pairs in a list that add up to a given number.

# numList = [1, 2, 3, 4, 5, 6, 7]
# targetNum  = 8
# pairList = []
# seen = set()
# for num in numList:
#     complement = targetNum-num
#     if complement in seen:
#         pairList.append(f"({complement},{num})")
#     seen.add(num)    
# print(pairList)  

# Question 05
# Write a program that rotates a list to the right by k positions.

# def rotate_list(numlist,k):
#     k = k % len(numlist)
#     return numlist[-k:] + numlist[:-k]
# k = int(input("Enter the number of positions to rotate: ")) 
# numList = [10, 20, 30, 40, 50]
# rotateList = rotate_list(numList,k)
# print("Rotate List :",rotateList)

# Question 06
# Write a program that finds the most frequently occurring element in a list.

# freqList = [3, 1, 3, 2, 1, 3, 4, 1, 1]
# freq = {}
# for num in freqList:
#     freq[num] = freq.get(num,0)+1
# maximumCount = max(freq,key=freq.get)
# print(f"The most frequent character is: '{maximumCount}' (Appeared {freq[maximumCount]} times)")    

# Question 07
# A list contains numbers from 1 to n, but one number is missing. Find the missing number.
# def findMissing(lst):
#     maxNum = max(lst)
#     minNum = min(lst)
    
#     listOne = [num for num in range(minNum+1, maxNum) if num not in lst]
    
#     return listOne

# numList = [1, 2, 3, 5, 6]
# print(findMissing(numList))

# def findMissing(list):
#     maxNum = list[0]
#     for i in list:
#         if i>maxNum:
#             maxNum=i
#     minNum = list[0]
#     for i in list:
#         if i<minNum:
#             minNum = i
#     listOne = []
#     for num in range(minNum+1,maxNum):
#         if num not in list:
#             listOne.append(num)
#     return str(listOne)[1:2]

# numList = [1,2,3,5,6]
# print(findMissing(numList))


# Question 08
# Write a program to find common elements between two lists without using set().
# list1 = [1,2,3,4,5]
# list2 = [2,3,4,5,6,1,7] 
# mergedTwo = list1+list2
# commonNum = {}
# intersection = []
# for num in mergedTwo:
#     commonNum[num] = commonNum.get(num,0)+1
#     if commonNum[num]>1:
#         intersection.append(num)
# print(intersection)

# Question 09
# Write a program that sorts a list in ascending order without using the built-in sort() function.
# listForSort = [5, 3, 8, 1, 2]
# minNum = min(listForSort)
# for i in range(len(listForSort)):
#     for j in range(len(listForSort) - 1 - i):
#         # print(j)
#         if listForSort[j] > listForSort[j+1]:
#            listForSort[j], listForSort[j + 1] = listForSort[j + 1], listForSort[j]

        
# print(listForSort)

# Question 10
# Write a program that finds the longest increasing subsequence (continuous numbers in increasing order).

# def logestIncreasingSubSequent(list):
#     if not list:
#         return []
#     longestSubSeq = []    
#     currentSubSeq = [list[0]]  # Start with the first number
#     for i in range(1,len(list)): 
#         if  list[i] > list[i-1]:  # If current number is greater, continue sequence
#             currentSubSeq.append(list[i])
#         else:
#             if len(currentSubSeq) > len(longestSubSeq): # Store the longest found
#                 longestSubSeq = currentSubSeq
#             currentSubSeq = [list[i]]   # Reset sequence  
#     #final check after loop
#     if len(currentSubSeq) > len(longestSubSeq): 
#         longestSubSeq = currentSubSeq
#     return longestSubSeq

# print(logestIncreasingSubSequent([5, 2, 3, 4, 8, 6, 7]))

# Question 11
# Write a program that finds all sets of 3 numbers that sum to zero.
# def threeSum(lists):
#     lists.sort() #Sort the List
#     triplets = []
#     for i in range(len(lists)-2):
#         if i>0 and lists[i] == lists[i-1]:  # Skip duplicates number
#             continue
#         left,right = i+1, len(lists)-1 # Two pointers

#         while left < right:
#             total = lists[i] + lists[left] + lists[right]
#             if total == 0:
#                 triplets.append([lists[i],lists[left],lists[right]])
#                 #Skip duplicates
#                 while left < right and lists[left] == lists[left+1]:
#                     left +=1
#                 while left <right and lists[right] == lists[left+1]:
#                     right -=1
                
#                 left +=1
#                 right -=1
#             elif total<0:
#                 left +=1
#             else:
#                 right -=1
#     return triplets

# lists = [-1, 0, 1, 2, -1, -4]
# print(threeSum(lists))


# Question 12
# Given a 2D list (matrix), print elements in a spiral order

# matrix =[
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]

# spiralOrder = []
# for arr in matrix:
#     for num in arr:
#         spiralOrder.append(num)
# print(spiralOrder)

# Question 13
# Write a program that finds all duplicate elements in a list.

# listNum = [4, 3, 2, 7, 8, 2, 3, 1]
# freqNum = {}
# duplicate = []
# for num in listNum:
#    freqNum[num] = freqNum.get(num,0)+1
#    if freqNum[num] > 1:
#         duplicate.append(num)
# print(duplicate) 

# Question 14
# Write a program that rearranges the elements of a list into a zigzag order (a < b > c < d > e ...).

# def zigzag(arr):
#     for i in range(len(arr) - 1):
#         if i % 2 == 0 and arr[i] > arr[i + 1]:  # a < b
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         elif i % 2 == 1 and arr[i] < arr[i + 1]:  # b > c
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr

# arr = [4, 3, 7, 8, 6, 2, 1]
# print(zigzag(arr))

# Question 15
# Write a program to find the k-th largest element in an unsorted list.

# print(numList[2-1])
def kthLargest(lists:list,k):
    lists.sort(reverse=True)
    return lists[k-1]


numList = [3, 2, 1, 5, 6, 4]
k=2
print(kthLargest(numList,k))