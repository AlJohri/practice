"""
Smallest Substring of All Characters

Question:

Given an array with unique characters arr and a string str, find the smallest substring of str containing all characters of arr.

Example:
arr: [x,y,z], str: xyyzyzyx
result: zyx

Implement your solution and analyze the runtime complexity

Tips:
If your peer is stuck, ask how can we determine if a given substring is valid (all chars from set are in it) and then ask how to apply that to a solution

If your peer is using a naive solution of checking all possible substrings, try to ask how can you avoid duplicate work

Make sure proper initializations are made

Watch for unnecessary variables and steps

For other solutions, make sure that any permutation of the characters in set can be found by the algorithm

make sure your peer understand why we should increase tail only after head is increased
"""

pass

"""
Solution:
We iterate the string from left to right, while using two indices - tailIndex and h.
At each iteration step, we examine the temp substring  [str.charAt(tailIndex), str.charAt(tailIndex+1) ..., str.charAt(h)]  and keep a copy of the shortest vaild substring we've seen so far.

To examine substrings we use 2 counters:
uniqueCounter (integer) - number of unique characters of arr in our temp substring
countMap (map/object/associative array - depends of your language of choice) - number of occurrences of each char from arr in our substring

function getShortestUniqueSubstring(arr, str):
   t = 0
   result = null
   uniqueCounter = 0
   countMap = new Map()
   # initialize countMap:
   for i from 0 to length(arr)-1:
      countMap.setValueOf(arr[i], 0)
   # scan str
   for h from 0 to length(str)-1:
      # handle the new head
      head = str.charAt(h)
      if countMap.keyExists(head) == false:
         continue
      headCount = countMap.getValueOf(head)
      if headCount == 0:
         uniqueCounter = uniqueCounter + 1
      countMap.setValueOf(head, headCount + 1)
      # push tail forward
      while uniqueCounter == length(arr):
         tempLength = h - t + 1
         if tempLength == arr.length:
            return str.substring(t, h)
         if (!result or tempLength < length(result)):
            result = str.substring(t, h)
         tail = str.charAt(t)
         if countMap.keyExists(tail):
            tailCount = countMap.getValueOf(tail) - 1
            if tailCount == 0:
               uniqueCounter = uniqueCounter - 1
            countMap.setValueFor(tail, tailCount)
         t = t + 1
   return result
Runtime Complexity: we're doing a linear iteration of both str and arr of lengths n and m respectively, so the runtime complexity is a linear O(n+m).

Space Complexity: depends of your implementation for the mapping, but generally: we're using countMap with m keys (the length of arr) plus few constant size counters - O(m) space complexity.

"""