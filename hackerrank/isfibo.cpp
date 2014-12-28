#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <unordered_map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

map<long,long> fibs;

long fibonacci(long n) {

	if (fibs[n]) return fibs[n];

    if (n <= 1) return n;
    long prev, next;
    
    if (fibs[n-1]) prev = fibs[n-1];
    else prev = fibonacci(n - 1);

	if (fibs[n-2]) next = fibs[n-2];
    else next = fibonacci(n - 2);

 	fibs[n] = prev + next;
 	return fibs[n];
}

bool isFibo(long num) {
	// convert to binary search instead of linear search?
	long prev, last; prev = last = 0;
	for (long i = 0; last <= num; i++) {
		prev = last;
		last = fibonacci(i);
	}
	if (prev == num || last == num) return true;
	return false;
}

int main() {
	string line; getline(cin, line);
    while (getline(cin, line)) {
    	long num = stol(line);
    	if (isFibo(num)) cout << "IsFibo" << endl;
    	else cout << "IsNotFibo" << endl;
    }

    return 0;
}