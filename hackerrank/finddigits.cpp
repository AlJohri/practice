#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int findDigits(int num) {
	int curDigit, numDivisible = 0, numCopy = num;
	do {
		curDigit = numCopy % 10;
		if (curDigit != 0 && num % curDigit == 0) numDivisible++;
	} while((numCopy /= 10));
	
	return numDivisible;
}

int main() {
	string line; getline(cin, line);
    while (getline(cin, line)) {
    	int num = stoi(line);
        cout << findDigits(num) << endl;
    }
    return 0;
}