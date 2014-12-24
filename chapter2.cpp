#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

template<class T>
class Node {
	public:
		Node* next;
		T data;
		Node() : next(NULL) {};
		Node(T mydata) : data(mydata), next(NULL) {};
		Node(T mydata, Node* mynext) : data(mydata), next(mynext) {};
		~Node();
};

template<class T>
void removeDuplicates(Node<T>* head) {
	unordered_map<T, bool> map;
	map[head->data] = true;
	Node<T>* cur = head;
	Node<T>* prev;
	while ((prev = cur, cur = cur->next)) {
		if (map[cur->data] == true) {
			prev->next = cur->next;
			free(cur);
			cur = prev->next;
		}
		else {
			map[cur->data] = true;
		}
	}
	return;
}

template<class T>
void removeDuplicates2(Node<T>* head) {
	Node<T>* dupCheck = head;
	Node<T>* cur = head;
	Node<T>* prev;
	do {
		cur = dupCheck;
		while ((prev = cur, cur = cur->next)) {
			if (cur->data == dupCheck->data) {
				prev->next = cur->next;
				free(cur);
			}
		}
	} while((dupCheck = dupCheck->next));
}

template<class T>
void printAll(Node<T>* head) {
	for (Node<T>* cur = head; cur != NULL; cur = cur->next) {
		cout << cur->data << ' ';
	}
	cout << endl;
}

Node<int>* createLinkedList() {
	Node<int>* g = new Node<int>(7);
	Node<int>* f = new Node<int>(5, g);
	Node<int>* e = new Node<int>(5, f);
	Node<int>* d = new Node<int>(4, e);
	Node<int>* c = new Node<int>(3, d);
	Node<int>* b = new Node<int>(2, c);
	Node<int>* a = new Node<int>(1, b);
	return a;
}

int main() {
	Node<int>* head1 = createLinkedList();
	printAll(head1);
	removeDuplicates(head1);
	printAll(head1);
	cout << endl;

	Node<int>* head2 = createLinkedList();
	printAll(head2);
	removeDuplicates2(head2);
	printAll(head2);
	cout << endl;
}

