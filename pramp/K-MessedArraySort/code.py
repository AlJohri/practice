"""
K-Messed Array Sort

Question:

Given an array arr of length n where each element is at most k places away from its sorted position,
Plan and code an efficient algorithm to sort arr.
Analyze the runtime and space complexity of your solution.

Example: n=10, k=2. The element belonging to index 6 in the sorted array, may be at indices 4, 5, 6, 7 or 8 on the given array.

If relevant data structures don't exist in your language of choice, you may assume their existence once you explain their concepts and operation to the interviewer and you both agree on its API.



Tips:
Try to help your peer think about the advantages of this nearly k-sorted array and can be useful with it

If your peer does not know about insertion sort or heap sort, make sure his knowledge section on the interview feedback reflect that

To get the best feedback rating on the problem solving section your peer should plan, explain and execute an O(n • log k) solution

If min-heap doesn't exist on the interview's coding language let your use a min-heap object as if it exists:
Valid operations are new MinHeap(), extractMin() and insert()

Watch for correct calculations and usage of array indices

If your peer is completely stuck, help the thought process by asking what can you do with a sliding window of size k+1
"""

pass

"""
Solution:
The suboptimal approach to solve is by using Insertion Sort:
We iterate the arr from left to right:
On each iteration we bring arr[i] to its place in the subarray arr[0,1,2 ... i], by shifting any subarray elements that are bigger than A[i] one place right.

function insertionSort(arr):
   for i from 1 to arr.length:
      j = i-1
      while (j >= 0 and arr[j] > arr[i]):
         arr[j+1] = arr[j] 
         j--
      arr[j+1] = arr[i]
   return arr
Runtime complexity: iteration over array of length n and switching at most k pairs for each iteration (by definition of the given array), takes O(n • k).
If k is constant and relatively small we can argue that it's actually close to a linear O(n) case.

Space complexity: constant O(1), all we need is 2 indices.

However, we can do better:

If we use a modified Heap Sort we can get better runtime complexity:
We define a virtual 'sliding window' of from the first k+1 elements of arr.
First we build a min heap from the elements in the window.
Then, we start sliding: on each step we extract the minimum from the heap, move the window one place right, place the min we've extracted into index that is now left to the window and insert the new element at the end of the window to the heap. We repeat that until the window reaches the end of the array, then we extract the minimum from the heap and place it on the next index of arr, until the heap is empty.

function kHeapSort(arr, k)
   h = new MinHeap()
   n = length(arr)
   for i from 0 to k:
      h.insert(arr[i])
   for i from k+1 to n-1:
      arr[i-(k+1)] = h.extractMin()
     h.insert(arr[i])
   for i from 0 to k:
     arr[n-k-1 + i] = h.extractMin()
   return arr
Runtime complexity:
Building a heap takes linear O(k) for k+1 elements.
Operating the heap later involves extracting min on a min-heap / inserting to the heap. These actions take O(log k) each. We do at least one of these actions n times, so the cost here is O(n • log k).
the overall runtime complexity of the heap solution is O(n • log k). again, if k is constant, we may argue the complexity is close to linear.

Space complexity:
we need to hold a min heap of  k+1 elements.
Since a heap is usually implemented with an array the space complexity is O(k+1).
However, we can implement and maintain the heap manually on our conceptual sliding window subarray. If we handled right, it can lead us to a constant O(1) space complexity.
"""