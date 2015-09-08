// Longest Increasing Subsequence
//
// output: [1, 3, 10, 11, 12]

#define size(a) sizeof(a)/sizeof(a[0]);

#include <iostream>

int main(int argc, char* argv[]) {
	// int arr[] = {1, 5, 4, 3, 10, 11, 12};
	int arr[] = {1, 5, 4, 3, 10, 11, 12, 2};

	int* newSequence;
	newSequence = longestIncreasingSubsequence(7, arr);
}

int* longestIncreasingSubsequence(int lenArray, int arr[]) {

	int** arrz;

	for(int i = 0; i < lenArray; i++) {
		arrz.append(longestIncreasingSubsequence(lenArray-i, arr))
	}

	int* currentSequence = arrz[0];
	for(int i = 1; i < size(arrz); i++) {
		if (size(arrz[i]) > size(currentSequence)) {
			currentSequence = arrz[i];
		}
	}

	return currentSequence;

}

// lic(j) = longest increasing subsequence ending at index j
// lic(j+1)

// if a_(j+1) > a_(j):
// 	L_j sequence + a_j + 1
// 