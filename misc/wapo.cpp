#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <numeric>

#include <vector>
#include <string>

#pragma GCC diagnostic ignored "-Wwrite-strings"

/*
Given a mixed array of numbers and alphanumeric terms, please implement a
function \ method that will return a sorted array such that the numbers are in
numeric order, and the alphanermic terms are in alphabetical order subject to
the following constraints:

	- For any index n in the array, the type of value at index n must be the same
	in the input and result arrays - e.g., given the input array
	{12, beta, 10, alpha} the positions (0,2) are numeric, while the positions
	(1,3) are alphanumeric, so the sorted result should be {10, alpha, 12, beta}

	- The maximum size of the input array is 1,000,000 items

	- Please use the following function \ method signatures:
		Java: public String[] sortMixedArray(String[] input)
		C \ C++: char ** sortMixedArray(const char** input, int size);
		Scala: def sortMixedArray(input Array[String]): Array[String]

Examples:
Input: {"10", "2", "washington", "1", "test", "11"};
Output: {"1", "2", "test", "10", "washington", "11"}

Input: {"6", "testing", "abc", "5", "1", "beta", "2321432", "zeta", "dog"};
Output: {"1", "abc", "beta", "5", "6", "dog", "2321432", "testing", "zeta"}
*/

template<typename T> void printArr(T *x, int size);
template<typename T> void printVec(std::vector<T> x);
char ** sortMixedArray(const char** input, int size);

int main(int argc, char const *argv[]) {
	const char *input1[] = {"10", "2", "washington", "1", "test", "11"};
	const char *input2[] = {"6", "testing", "abc", "5", "1", "beta", "2321432", "zeta", "dog"};

	char **output1 = sortMixedArray(input1, 6);
	char **outputt = sortMixedArray(input2, 9);

	return 0;
}

template<typename T> void printArr(T *x, int size) {
	for(std::size_t i = 0 ; i<size ; ++i) std::cout << x[i] << " ";
	std::cout << std::endl;
}

template<typename T> void printVec(std::vector<T> x) {
	for (typename std::vector<T>::const_iterator i = x.begin(); i != x.end(); ++i)
		std::cout << *i << ' ';
    std::cout << std:: endl;
}

char ** sortMixedArray(const char** input, int size) {
	std::vector<bool> types(size); // vector of booleans, where true is numeric
	std::vector<int> numerics; // filtered vector of numeric integers
	std::vector<std::string> alphanumerics; // filtered vector of alphanumerics strings

	for(std::size_t i = 0 ; i<size; ++i) {
		char *ptr; long int num = strtol(input[i], &ptr, 10);

		types[i] = (*ptr == 0); // if ptr is 0, x is a number
		if (types[i]) numerics.push_back(num);
		else alphanumerics.push_back(std::string(input[i]));
	}

	std::sort(numerics.begin(), numerics.end()); // O(nlogn)
	std::sort(alphanumerics.begin(), alphanumerics.end()); // O(nlogn)

	std::cout << "Input: "; printArr(input, size);
	std::cout << "Types (true is numeric): "; printVec<bool>(types);
	std::cout << "Numerics: "; printVec<int>(numerics);
	std::cout << "Alphanumerics: "; printVec<std::string>(alphanumerics);

	std::vector<std::string> result(size);

	int numericCounter, alphanumericCounter;
	numericCounter = alphanumericCounter = 0;

	for(std::size_t i = 0; i < size; ++i) {
		if (types[i]) {
			result[i] = std::to_string(numerics[numericCounter]);
			numericCounter++;
		}
		else {
			result[i] = alphanumerics[alphanumericCounter];
			alphanumericCounter++;
		}
	}

	std::cout << "Sorted Result (strings): "; printVec<std::string>(result);

	std::vector<const char *> retValue(size);
	for(std::size_t i = 0; i < size; ++i) retValue[i] = result[i].c_str();

	std::cout << "Sorted Result (c-strings): "; printVec<const char*>(retValue);

	std::cout << std::endl;

	// const_cast because of the function signature explicitly given in the problem
	// requires const** return type (not const char**)
	return const_cast<char**>(retValue.data());
}