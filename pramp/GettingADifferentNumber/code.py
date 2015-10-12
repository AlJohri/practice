"""
Getting a Different Number

Question:

Given an array arr of n unique integers, how can you most efficiently find an
integer that is not in the array?

Your solution should return such an integer or null if arr contains all
possible integers.
Analyze the runtime and space complexity of your solution.

Tips:
If your peer is stuck ask what do you both know about the numbers in arr.
answer: integers and there are n such numbers. Then try to ask how can you find
the n+1th number and so on

If it doesn't help ask if your peer about the pigeonhole principle and how can
this be applied. If your peer is not familiar with it, this is the time to explain :)

If your peer is still stuck ask how can you use a hash function to find a
number that is not in arr.

If you have time you can ask your peer how can you generate more numbers that
are not in arr.
This can be done either by building arr2 as a longer array or by using the formula
j + (n+1)^p  from the solution.
"""

def getAnotherNumber(arr):
	pass

"""
Solution:

A naive solution is to randomize numbers. However, this is not a good approach:
if n is very large we'll have to search the random numbers in that array many
times.

Another simple solution is to keep record of the minimum/maximum while
iterating over all numbers in arr and then produce numbers smaller/larger than
all numbers in arr. However, this won't work if the minimum number is -MAX_INT
and the maximum number is MAX_INT. Another iteration tactic is to return the
sum of all numbers, but it won't work for a mix of negative and positive
numbers or for an entire array of zeros.

A better approach is applying the pigeonhole principle and using a similar
approach to hashing.
We create an array arr2 of length n+1. If we use a hash function to map every
number from arr to an index of arr2 then from the pigeonhole principle at least
one cell in arr2 will remain empty.
We can use a simple hash function like f(x) = x mod (n+1) for this mapping.
Then, for any index j of an empty cell of arr2 we can  guarantee that the
integer j is not in arr.

Moreover, any result of j + (n+1)m for any integer m that is within the limits
[-MAX_INT, MAX_INT] is a number that is not in arr (this is derived directly
from mod definition).

function getAnotherNumber(arr):
   n = length(arr)
   if (n == 2*MAX_INT): // all possible integers are in arr
      return null
   arr2 = []
   for i from 0 to n:
      arr2[i] = 0
   for i from 0 to n-1:
      num = arr[i]
      arr2[num % (n+1)] = 1
   for i from 0 to n:
      if arr2[i] == 0:
         return i

Runtime Complexity: going over array of length n or n+1 3 times, we get a
linear O(n) run time complexity.

Space Complexity: from using an additional array of length n+1, we get a linear
O(n) space complexity.
"""