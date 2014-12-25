#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

template<class T>
class Node {
	public:
		Node* next;
		T data;
		bool checked;
		Node() : next(NULL) {};
		Node(T mydata) : data(mydata), next(NULL) {};
		Node(T mydata, Node* mynext) : data(mydata), next(mynext) {};
		~Node() {};
};

template<class T>
void appendItem(Node<T>*&head, Node<T>*&tail, Node<T>*cur) {
	if (head == NULL) { head = cur; tail = cur; }
	else { tail->next = cur; tail = cur; }
}

template<class T>
void removeItem(Node<T>*& head, T item) {
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
void removeNode(Node<T>*& head, Node<T>*& n) {
	Node<T>* cur = head;
	if (head == n) {
		head = head->next;
		delete cur;
		return;
	}
	Node<T>* prev;
	while ((prev = cur, cur = cur->next)) {
		if (cur == n) {
			prev->next = cur->next;
			delete cur;
			cur = prev;
			return; // deletes only one instance of item
		}
	}
	return;
}

// 2.1 Write code to remove duplicates from an unsorted linked list.
// FOLLOW UP
// How would you solve this problem if a temporary buffer is not allowed?

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

// no buffer
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

// 2.2 Implement an algorithm to find the kth to last element of a singly linked list.

template<class T>
T findKthElement(Node<T>* head, int k) {
	Node<T>* cur = head;
	Node<T>* prev = head;
	for (int i = 0; i < k; i++) cur = cur->next;
	while (cur->next) { prev = prev->next; cur = cur->next; }
	return prev->data;
}

// 2.3 Implement an algorithm to delete a node in the middle of a singly linked list,
// given only access to that node.
// EXAMPLE
// Input: the node c from the linked list a->b->c->d->e
// Result: nothing is returned, but the new linked list looks like a- >b- >d->e

template<class T>
void deleteNode(Node<T>*& n) {
	Node<T>* nodeToDelete = n->next;
	if (n == NULL || nodeToDelete == NULL) return;
	n->data = nodeToDelete->data;
	n->next = nodeToDelete->next;
	delete nodeToDelete;
	return;
}

// 2.4 Write code to partition a linked list around a value x, such that all nodes less 
// than x come before all nodes greater than or equal to x.

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

// 2.5 You have two numbers represented by a linked list, where each node contains a
// single digit. The digits are stored in reverse order, such that the Ts digit is at the
// head of the list. Write a function that adds the two numbers and returns the sum
// as a linked list.

Node<int>* addLists(Node<int>* l1, Node<int>* l2) {
	Node<int>* l3Head = NULL; Node<int>* l3Tail = NULL;
	int curRemainder = 0;
	while (true) {
		if (l1 && l2) {
			int curSum = l1->data + l2->data + curRemainder;
			curRemainder = 0;
			appendItem(l3Head, l3Tail, new Node<int>(curSum % 10));
			curRemainder += curSum/10;
		}
		else if (l1 && !l2) {
			appendItem(l3Head, l3Tail, new Node<int>(l1->data));
		}
		else if (!l1 && l2) {
			appendItem(l3Head, l3Tail, new Node<int>(l2->data));
		}
		else if (!l1 && !l2 && curRemainder > 0) {
			appendItem(l3Head, l3Tail, new Node<int>(curRemainder));
			curRemainder = 0;
		}
		else {
			return l3Head;
		}
		l1 = l1->next;
		l2 = l2->next;
	}
}

// 2.6 Given a circular linked list, implement an algorithm which returns the node at the
// beginning of the loop.

template<class T>
Node<T>* findLoopStart(Node<T>* head) {
	Node<T>* slow = head;
	Node<T>* fast = head;

	do {
		slow = slow->next;
		fast = fast->next->next;
	} while (slow != NULL && fast != NULL && fast->next != NULL && slow != fast);

	if (slow == fast && slow != NULL && fast != NULL) {
		Node<T>* loopPtr = slow;
		loopPtr->checked = true;
		Node<T>* cur = loopPtr->next;
		while (cur != loopPtr) { cur->checked = true; cur = cur->next; }
		Node<T>* cur2 = head;
		while((cur2 = cur2->next)) {
			if (cur2->checked == true) return cur2;
		}
	}
	else {
		return NULL;
	}
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
	cout << "removeDuplicates" << endl;
	Node<int>* head1 = createLinkedList();
	printAll(head1);
	removeDuplicates(head1);
	printAll(head1);
	cout << endl;

	cout << "removeDuplicates2" << endl;
	Node<int>* head2 = createLinkedList();
	printAll(head2);
	removeDuplicates2(head2);
	printAll(head2);
	cout << endl;

	cout << "findKthElement" << endl;
	Node<int>* head3 = createLinkedList();
	printAll(head3);
	cout << "find 0th" << endl;
	cout << findKthElement(head3, 0) << endl;
	cout << "find 2nd" << endl;
	cout << findKthElement(head3, 2) << endl;
	cout << "find 4th" << endl;
	cout << findKthElement(head3, 4) << endl;
	cout << endl;

	cout << "deleteNode (without access to head)" << endl;
	Node<int>* head4 = createLinkedList();
	printAll(head4);
	Node<int>* tmp = head4->next->next;
	cout << "remove node with value: " << tmp->data << endl;
	deleteNode(tmp);
	printAll(head4);
	cout << endl;

	cout << "removeNode" << endl;
	Node<int>* head5 = createLinkedList();
	printAll(head5);
	Node<int>* first5 = head5;
	Node<int>* second5 = head5->next;
	Node<int>* third5 = head5->next->next;
	Node<int>* fourth5 = head5->next->next->next;
	cout << "remove fourth: " << fourth5->data << endl;
	removeNode(head5, fourth5);
	printAll(head5);
	cout << "remove second: " << second5->data << endl;
	removeNode(head5, second5);
	printAll(head5);
	cout << "remove first: " << first5->data << endl;
	removeNode(head5, first5);
	printAll(head5);
	cout << "remove third: " << third5->data << endl;
	removeNode(head5, third5);
	printAll(head5);
	cout << endl;

	cout << "removeItem" << endl;
	Node<int>* head6 = createLinkedList();
	printAll(head6);
	cout << "remove 2" << endl;
	removeItem(head6, 2);
	printAll(head6);
	cout << "remove 5" << endl;
	removeItem(head6, 5);
	printAll(head6);
	cout << "remove 5" << endl;
	removeItem(head6, 5);
	printAll(head6);
	cout << "remove 4" << endl;
	removeItem(head6, 4);
	printAll(head6);
	cout << "remove 1" << endl;
	removeItem(head6, 1);
	printAll(head6);
	cout << endl;

	cout << "pivotList" << endl;
	Node<int>* head7_6 = new Node<int>(6);
	Node<int>* head7_5 = new Node<int>(1, head7_6);
	Node<int>* head7_4 = new Node<int>(4, head7_5);
	Node<int>* head7_3 = new Node<int>(7, head7_4);
	Node<int>* head7_2 = new Node<int>(3, head7_3);
	Node<int>* head7_1 = new Node<int>(5, head7_2);
	Node<int>* head7 = new Node<int>(2, head7_1);
	printAll(head7);
	pivotList(head7, 3);
	printAll(head7);
	cout << endl;

	cout << "addLists" << endl;
	Node<int>* head8_2 = new Node<int>(6);
	Node<int>* head8_1 = new Node<int>(1, head8_2);
	Node<int>* head8 = new Node<int>(7, head8_1);
	printAll(head8);
	Node<int>* head9_2 = new Node<int>(2);
	Node<int>* head9_1 = new Node<int>(9, head9_2);
	Node<int>* head9 = new Node<int>(5, head9_1);
	printAll(head9);
	Node<int>* head10 = addLists(head8, head9);
	printAll(head10);
	cout << endl;

	cout << "findLoopStart" << endl;
	Node<int>* head11_7 = new Node<int>(8);
	Node<int>* head11_6 = new Node<int>(7, head11_7);
	Node<int>* head11_5 = new Node<int>(6, head11_6);
	Node<int>* head11_4 = new Node<int>(5, head11_5);
	Node<int>* head11_3 = new Node<int>(4, head11_4);
	Node<int>* head11_2 = new Node<int>(3, head11_3);
	Node<int>* head11_1 = new Node<int>(2, head11_2);
	Node<int>* head11 = new Node<int>(1, head11_1);
	head11_7->next = head11_2; // loop
	Node<int>* head12 = createLinkedList();

	Node<int>* head11LoopStart = findLoopStart(head11);
	Node<int>* head12LoopStart = findLoopStart(head12);

	if (head11LoopStart != NULL) cout << "head11 LoopStart " << head11LoopStart->data << endl;
	else cout << "head11 has no loop" << endl;
	if (head12LoopStart != NULL) cout << "head12 LoopStart " << head12LoopStart->data << endl;
	else cout << "head12 has no loop" << endl;

}

