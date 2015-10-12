"""
Find The Duplicates

Question:

Given two arrays of US social security numbers: Arr1 and Arr2 of lengths n and m
respectively, how can you most efficiently compute an array of all persons included
on both arrays?

Solve and analyze the complexity for 2 cases:
1. m ≈ n - lengths are approximately the same
2. m ≫ n - one is much longer than the other

Tips:
As in any array iteration, check for proper indices limit and for covering all
elements within the array

If your peer is stuck, ask for the brute force solution and then ask how can you
do better. Another clue is to ask your peer to use the fact that arrays are sorted

If your peer is making mistakes about complexity try to see if they can detect
it before being told. ask them to explain, and if it doesn't help you can ask: Are you sure?

Some of the solutions for this kind of question may involve hashing one array
and then searching its hash table for every item of the second array. For the first
case (about the same length) the joint linear scan is better since you don't need to
build the hash and maintain it. For the second case (one array is much longer than the
other) it doesn't make any sense.

"""

pass

"""

Solution:

The brute force solution is looping over one array, then looping on the other for each
number of the first while storing the matches. That involves O(n⋅m) runtime complexity - very
inefficient.

1. m ≈ n
We can leverage the sorted order of the arrays and loop over both in-order at the same time.
By increasing the index of the array with the current smaller value every time we can be sure
not to miss any duplicate:

function findDuplicates1(Arr1, Arr2):   duplicates = []
   i = 0
   j = 0
   while i < length(Arr1) and j < length(Arr2):
      if Arr1[i] == Arr2[j]:
         duplicated.append(Arr1[i])
         i = i + 1
         j = j + 1
      else if Arr1[i] < Arr2[j]:
         i = i + 1
      else:
         j = j + 1
   return duplicates
Runtime Complexity: liner O(n+m).

2. m ≫ n
When one array is much longer than the other we should try to avoid a linear iteration over
the longer one.
Since arrays are sorted, we can do a linear iteration over the shorter and perform binary
search for it on the longer array while storing all the matches.

function findDuplicates2(Arr1, Arr2):
   duplicates = []
   for number in Arr1:
      if binarySearch(Arr2, number) != -1:
         duplicates.append(number);
   return duplicates

function binarySearch(arr, num):
    begin = 0
    end = length(arr)
    while (begin <= end):
       mid = round((begin+end)/2)
       if arr[mid] < num:
          begin = mid + 1
       else if arr[mid] == num:
          return mid
       else:
          end = mid - 1
    return -1
Runtime Complexity: O(n⋅log m). Since m ≫ n and m ≫ log m, O(n⋅log m) should be
asymptotically better than O(n+m).

"""