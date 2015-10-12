"""
Shifted Array Search

Question:

1. Find a given number num in a sorted array arr:
arr = [2, 4, 5, 9, 12, 17]

2. If the sorted array arr is shifted left by an unknown offset and you don't have a pre-shifted copy of it, how would you modify your method to find a number in the shifted array?
shiftArr = [9, 12, 17, 2, 4, 5]

Explain and code an efficient solution and analyze its runtime complexity
if num doesn't exist in the array, return -1



Tips:
The first part of the question is there to make sure that your peer understands binary search. Make sure this is the case

If your peer doesn't understand binary search go ahead and explain it, but be sure to reduce your rating on the knowledge section of the interview feedback 

A common attempt to reach a solution is by concatenating the shifted array to itself (will produce [9, 12, 17, 2, 4, 5, 9, 12, 17, 2, 4, 5] according to the example)
While this seems right, it's then difficult to tune what half of the array to focus on next (left/right). Be aware of that if your peer tries it.

Watch for mistakes with index calculations (division results not rounded, out of array bounds, forgotten indices etc.)

If uncertain of different solution approaches taken by your peer, ask your peer to explain why the solution is always correct for all cases and examine it together

Correct solution must involve O(log n) runtime complexity

"""

pass

"""

Solution:
1. Solved by plain binary search:

function binarySerach(arr, num):
   while (begin <= end):
      mid = round((begin+end)/2)
      if arr[mid] < num:
         begin = mid + 1
      else if arr[mid] == num:
         return mid
      else:
         end = mid - 1
   return -1
2. For shifted arrays, binary search isn't as simple.
One solution is to split the shiftArr to 2 sub-arrays:

the sub-array ([9, 12, 17] on the example)
the other sub-array ([2, 4, 5] on the example).
Once the array is split we can apply binary search only on the relevant sub-array.
The relevant sub-array (of length [n]) would satisfy: subArr[0] ≤ num ≤ subArr[n-1].

To make the split we need the index of the first number in arr (the non-shifted array) in shiftArr (2 in the example).
The number on this index is the only one that is smaller than its left neighbor shiftArr[i] ≤ shiftArr[i-1] (2 < 17 on the example).

To find this index we use a modified binary search:
On each step we check if the current shiftArr is smaller than it's left neighbor. If it does - we've found the index we need.
Otherwise, we determine what half of the array to focus on by comparing shiftArr[mid] to the first number of shiftArr[0]. This comparison will tell us if the current mid index is part of the shifted sub-array or the other sub-array.

function shiftedArrSearch(shiftArr, num):
   originalFirst = getOrigFirst(shitfArr)
   if num >= shiftArr[0]:
      arr = shiftArr.subArr(0, originalFirst-1)
      return binarySerach(arr, num)
   else:
      n = length(shiftArr)
      arr = shiftArr.subArr(originalFirst-1, n-1)
      return binarySearch(arr, num)

function getOrigFirst(arr):
   begin = 0
   end = length(arr)
   while (begin <= end):
      mid = round((begin+end)/2)
      if (mid == 0 or arr[mid] < arr[mid-1]):
         return mid
      if arr[mid]  arr[0]:
         begin = mid + 1
      else:
         end = mid - 1
   return 0
Runtime Complexity:
1. since we decrease our input size in half on each iteration step, the runtime complexity of binary search is O(log n).
2. doing 2 binary searches (1 modified and 1 typical), the runtime complexity is O(log n).

"""