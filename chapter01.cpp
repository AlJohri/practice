#include <iostream>
#include <string>
using namespace std;

// 1.1
// Implement an algorithm to determine if a string has all unique 
// characters. What if you cannot use additional data structures?

bool hasUniqueChars(string s) {
	for (int i = 0; i < s.length(); i++) {
		for (int j = i+1; j < s.length(); j++) {
			if (s[i] == s[j]) return false;
		}
	}
	return true;
}

// practice using char* instead of string
bool hasUniqueChars2(char* str) {
	for (char* ptr1 = str; *ptr1 != '\0'; ptr1++) {
		for (char* ptr2 = ptr1+1; *ptr2 != '\0'; ptr2++) {
			if (*ptr1 == *ptr2) return false;
		}
	}
	return true;
}

// 1.2
// Implement a function void reverse(char* str) in C or C++ which
// reverses a null terminated string.

// in place
void reverse(char* str) {
	char* start = str;
	char* end = str;
	while (*end!='\0') end++;
	end--;
	while (start < end) {
		char tmp = *start;
		*start = *end;
		*end = tmp;
		start++;
		end--;
	}
	return;
}

// pass in char*
void reverse2(char* str, char* output) {
	for (int i = strlen(str)-1, j = 0; i > -1; i--, j++) {
		output[j] = str[i];
	}
	return;
}

// 1.3 Given two strings, write a method to decide if one is a permutation of the other.

bool isPermutation(string str1, string str2) {
	if (str1.length() != str2.length()) return false;
	string str1Sorted = str1;
	string str2Sorted = str2;
	sort(str1Sorted.begin(), str1Sorted.end());
	sort(str2Sorted.begin(), str2Sorted.end());
	if (str1Sorted == str2Sorted) return true;
	return false;
}

// 1.4 Write a method to replace all spaces in a string with'%20'. You may assume that
// the string has sufficient space at the end of the string to hold the additional
// characters, and that you are given the "true" length of the string. (Note: if implementing
// in Java, please use a character array so that you can perform this operation
// in place.)

void replaceAllSpaces(string &s) {
	int index = 0;
	while (true) {
		index = s.find(' ', index);
		if (index == -1) break;
		s.replace(index, 1, "%20");
		index++;
	}
	return;
}

// 1.5 Implement a method to perform basic string compression using the counts
// of repeated characters. For example, the string aabcccccaaa would become
// a2blc5a3. If the "compressed" string would not become smaller than the original
// string, your method should return the original string.

string compress(string s) {
	int index = 0;
	string compressedString = "";
	while (index < s.length()) {
		string currentChar = string(1, s[index]);
		int currentCount = 1;
		while (s[index] == s[index+1]) {
			currentCount++; index++;
		}
		compressedString.append(currentChar);
		compressedString.append(to_string(currentCount));
		index++;
	}
	if (s.length() < compressedString.length()) return s;
	return compressedString;
}

// 1.6 Given an image represented by an NxN matrix, where each pixel in the image is
// 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
// place?

// DOESN'T WORK!

template<typename T, int rows, int cols>
void rotateMatrix(T (&array)[rows][cols]) {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			int iPrime = j;
			int jPrime = i;
			T tmp = array[iPrime][jPrime];
			array[iPrime][jPrime] = array[i][j];
			array[i][j] = tmp;
		}
	}
	return;
}

// 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
// and column are set to 0.

template<typename T, int rows, int cols>
void clearMatrixRowAndColumn(T (&array)[rows][cols]) {
	int rowsToClear[rows], columnsToClear[cols];

	memset(rowsToClear, 0, rows*sizeof(T));
	memset(columnsToClear, 0, cols*sizeof(T));

	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (array[i][j] == 0) {
				rowsToClear[i] = 1; columnsToClear[j] = 1;
			}
		}
	}

	for (int i = 0; i < rows; i++)
		for (int j = 0; j < cols; j++)
			if (rowsToClear[i] || columnsToClear[j])
				array[i][j] = 0;
}

// 1.8 Assume you have a method isSubstring which checks if one word is a
// substring of another. Given two strings, si and s2, write code to check if s2 is
// a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle"is a rotation
// of "erbottlewat").

bool isRotation(string s1, string s2) {
	string rotatedS1 = s1 + s1;
	if (rotatedS1.find(s2) != -1) return true;
	return false;
}

// Utilities for 1.6 and 1.7

template <typename T, int rows, int cols>
void print(T (&array)[rows][cols]) {
    for (int i = 0; i < rows; ++i) {
    	for (int j = 0; j < cols; ++j)
    		cout << array[i][j] << ' ';
    	cout << endl;
    }
}

int main() {
	char world[] = "world";
	char helloWorld[] = "hello world";

	cout << hasUniqueChars(world) << endl;
	cout << hasUniqueChars(helloWorld) << endl;
	cout << endl;

	cout << hasUniqueChars2(world) << endl;
	cout << hasUniqueChars2(helloWorld) << endl;
	cout << endl;
	
	char output[strlen(world)];
	cout << world << endl;
	reverse2(world, output);    
	cout << output << endl;
	cout << endl;

	cout << helloWorld << endl;
	reverse(helloWorld);
	cout << helloWorld << endl;
	reverse(helloWorld); // revert
	cout << helloWorld << endl;
	cout << endl;

	char rowdl[] = "rowdl";
	cout << isPermutation(world, rowdl) << endl;
	cout << isPermutation(world, helloWorld) << endl;
	cout << endl;

	string wordWithSpaces = "hell ooo woo rlddd";
	cout << wordWithSpaces << endl;
	replaceAllSpaces(wordWithSpaces);
	cout << wordWithSpaces << endl;
	cout << endl;

	string stringWithRepatedChars = "aabcccccaaa";
	cout << stringWithRepatedChars << endl;
	cout << compress(stringWithRepatedChars) << endl;
	cout << helloWorld << endl;
	cout << compress(helloWorld) << endl;
	cout << endl;

	int matrix[4][4] = {{1,0,3,4}, {1,2,3,4}, {1,2,3,4}, {1,2,3,4}};

	string matrix2[4][4] = {{"00","01","02","03"}, {"10","11","12","13"}, {"20","21","22","23"}, {"30","31","32","33"}};
	print(matrix2);
	cout << endl;
	rotateMatrix(matrix2);
	print(matrix2);
	cout << endl;

	print(matrix);
	cout << endl;
	rotateMatrix(matrix);
	print(matrix);
	cout << endl;

	print(matrix);
	cout << endl;
	clearMatrixRowAndColumn(matrix);
	print(matrix);
	cout << endl;

	char erbottlewat[] = "erbottlewat";
	char waterbottle[] = "waterbottle";
	cout << erbottlewat << endl;
	cout << waterbottle << endl;
	cout << isRotation(erbottlewat, waterbottle) << endl;
	cout << isRotation(world, rowdl) << endl;
	cout << endl;

	return 0;
}
