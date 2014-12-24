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
		~Node() {};
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
			delete cur;
			cur = prev;
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
				delete cur;
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

template<class T>
T findKthElement(Node<T>* head, int k) {
	Node<T>* cur = head;
	Node<T>* prev = head;
	for (int i = 0; i < k; i++) cur = cur->next;
	while (cur->next) { prev = prev->next; cur = cur->next; }
	return prev->data;
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

template<class T>
void removeNode(Node<T>*& head, T item) {
	Node<T>* cur = head;
	if (head->data == item) {
		head = head->next;
		delete cur;
	}
	Node<T>* prev;
	while ((prev = cur, cur = cur->next)) {
		if (cur->data == item) {
			prev->next = cur->next;
			delete cur;
			cur = prev;
			return; // deletes only one instance of item
		}
	}
	return;
}

template<class T>
void appendItem(Node<T>*&head, Node<T>*&tail, Node<T>*cur) {
	if (head == NULL) { head = cur; tail = cur; }
	else { tail->next = cur; tail = cur; }
}

template<class T>
void pivotList(Node<T>*&head, T pivot) {
	Node<T>* headLeft = NULL; Node<T>* tailLeft = NULL;
	Node<T>* headPivot = NULL; Node<T>* tailPivot = NULL;
	Node<T>* headRight = NULL; Node<T>* tailRight = NULL;

	Node<T>* cur = head;
	do {
		if (cur->data == pivot) appendItem(headPivot, tailPivot, cur);
		else if (cur->data > pivot) appendItem(headRight, tailRight, cur);
		else if (cur->data < pivot) appendItem(headLeft, tailLeft, cur);
	} while ((cur = cur->next));

	tailLeft->next = headPivot;
	tailPivot->next = headRight;
	head = headLeft;

	return;
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

	Node<int>* head3 = createLinkedList();
	printAll(head3);
	cout << findKthElement(head3, 0) << endl;
	cout << findKthElement(head3, 2) << endl;
	cout << findKthElement(head3, 4) << endl;
	cout << endl;

	Node<int>* head4 = createLinkedList();
	printAll(head4);
	removeNode(head4, 2);
	printAll(head4);
	removeNode(head4, 5);
	printAll(head4);
	removeNode(head4, 5);
	printAll(head4);
	removeNode(head4, 4);
	printAll(head4);
	removeNode(head4, 1);
	printAll(head4);
	cout << endl;

	Node<int>* g = new Node<int>(6);
	Node<int>* f = new Node<int>(1, g);
	Node<int>* e = new Node<int>(4, f);
	Node<int>* d = new Node<int>(7, e);
	Node<int>* c = new Node<int>(3, d);
	Node<int>* b = new Node<int>(5, c);
	Node<int>* head5 = new Node<int>(2, b);
	printAll(head5);
	pivotList(head5, 3);
	printAll(head5);
	cout << endl;
}

