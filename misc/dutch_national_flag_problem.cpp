// https://en.wikipedia.org/wiki/Dutch_national_flag_problem

#include <iostream>

using namespace std;

template <typename T> void semiSort(T arr[], int lenArray, T pivot);

int main(int argc, char *argv[]) {
	// int arr[] = {2, 7, 4, 3, 1, -1, 0, 9};
	// int arr[] = {2, 7, 9, 1, 3, -1, 0, 4, -10};
	// int arr[] = {6, 5, 6, 6, 3, 9, 8, 10};
	// int arr[] = {1, 2, 3, 4, 5};
	int arr[] = {7, 8, 9, 10, 11};
	int lenArray = 5;
	int pivot = 6;

	for(int i = 0; i < lenArray; i++) cout << arr[i] << " ";
	cout << endl;
	semiSort<int>(arr, lenArray, pivot);
	for(int i = 0; i < lenArray; i++) cout << arr[i] << " ";
	cout << endl;
};

template <typename T>
void semiSort(T arr[], int lenArray, const T &pivot) {
	int i = 0;
	int rightHalfIndex = lenArray-1;
	int pivotCounter = 0;

	while (i < rightHalfIndex) {
		if (arr[i] < pivot) {
			i++;
		}
		else { // (arr[i] > pivot)
			swap<T>(arr[i], arr[rightHalfIndex]);
			rightHalfIndex--;
		}
	}
}

template <typename T>
void swap(T &a, T &b) {
	T temp = a;
	a = b;
	b = temp;
}
