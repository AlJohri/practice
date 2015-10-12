"""
Array Index & Element Equality

Question:

Given an array of sorted distinct integers named arr, write a function that
returns an index i in arr for which arr[i] = i or -1 if no such index exists.

Implement the most efficient solution possible, prove the correctness of your
solution and analyze its runtime complexity (in terms of n - the length of arr).

Examples:

Given arr = [-8,0,2,5] the function returns 2, since arr[2] = 2
Given arr = [-1,0,3,6] the function returns -1, since no index in arr
satisfies arr[i] = i


Tips:
While coding the solution is simple, this question takes a solid understanding
of binary search and what it takes to use it.
Make sure that your peer can tackle this issue and rate him accordingly (on
both the problem solving and knowledge sections of the interview feedback)

As in any array iteration, check for proper indices limit and for covering
all elements within the array

the solution is not complete without both getting a logarithmic runtime
complexity and proving why this can be done. Your peer may not be familiar with
the notion of strictly monotonically increasing sequence but should be able to
clearly explain the correctness of their solution (do share this notion with
   after your peer answer if it wasn't mentioned)

The subtraction trick is elegant but it's not a must, you can instead check if
arr[i] equal to, lower than or greater than i as the condition to return i,
reiterate on the upper half or reiterate on the lower half respectively.

If your peer is stuck beyond the naive solution try to ask how can you usually
perform a more efficient scan on a sorted array (binary search, of course)
"""

pass

"""
Solution:

The naive solution is to iterate on all items in the array and check the
condition. This takes linear O(n) runtime complexity.

To do better, we should recognize that both the sequence of i (array indices)
and the sequence of arr[i] (array values) are strictly monotonically increasing
sequences.
If we subtract i from both sides of the equation arr[i] = i we get
arr[i] - i = 0.
Since the difference arr[i] - i = 0 consists of strictly monotonically
increasing sequences it is a strictly monotonically increasing sequence by
itself.
We can use this to define another array diffArr where diffArr[i] = arr[i] - i
and perform a binary search for 0 on diffArr.
We don't need to really create this array, and can just modify the binary
search condition to arr[i] - i = 0 (instead of the condition diffArr[i] = 0).

So why is it important that for the search condition to form a strictly
monotonically increasing squence?
On each step of this modified binary search where the current index is j, to
cut our array limit in half and drop the other half we must be confident that:

arr[j] - j ≥ arr[q] - q  for every index  j > q
arr[j] - j ≤ arr[p] - p  for every index  j < p
This can be easily established by showing that arr[i] - i is a strictly
monotonically increasing sequence.

After proving its correctness, we can implement the search:

function indexEqualsValueSearch(arr):
   begin = 0
   end = arr.length
   while (begin <= end):
      i = round((begin+end)/2)
      if (arr[i] - i < 0):
         begin = i+1
      else if (arr[i] - i == 0):
         return i
      else:
          end = i-1
return -1

Runtime Complexity: O(log n) since we use a binary search where the input
size is reduced in half on each step. Our modification of calculating
arr[i] - i instead of arr[i] is done in constant time and adds nothing.
"""