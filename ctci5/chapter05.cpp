#include <iostream>

using namespace std;

void print_char_as_binary(char ch) {
	int i = CHAR_BIT;
	while (i > 0) {
		-- i;
		cout << (ch & (1 << i) ? '1' : '0');
	}
}

int main() {
	print_char_as_binary('w'); cout << endl;
	// print_char_as_binary('u'); cout << endl;
	cout << bitset<8>(1 << 0) << endl;
	cout << ('w' & (1 << 0)) << endl;
	cout << bitset<8>(1 << 8) << endl;
	cout << ('w' & (1 << 8)) << endl;
	// cout << bitset<8>(-2) << endl;
	// int test = 1;
	// cout << bitset<8>(-2) << endl;
	// cout << bitset<8>(-1) << endl;
	// cout << endl;
	// cout << bitset<8>(0) << endl;
	// cout << bitset<8>(1) << endl;
	// cout << bitset<8>(2) << endl;
	// cout << bitset<8>(3) << endl;
	// cout << bitset<8>(4) << endl;
	// cout << bitset<8>(5) << endl;
	// cout << bitset<8>(6) << endl;
	// cout << bitset<8>(7) << endl;
	// cout << bitset<8>(8) << endl;
	// cout << endl;
	// cout << bitset<8>(16) << endl;
	// cout << bitset<8>(32) << endl;
	// cout << bitset<8>(64) << endl;
	// cout << bitset<8>(128) << endl;
}
