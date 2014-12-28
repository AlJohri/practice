#include <iostream>

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

template <typename T>
class Stack {
	public:
		Node<T>* top;
		void push(T item) {
			Node<T>* node = new Node<T>(item);
			node->next = this->top;
			this->top = node;
		} ;
		void pop() {
			this->top = this->top->next;
		};
		T peek() {
			return this->top->data;
		} ;
		Stack() : top(NULL) {};
		~Stack() {};
};

template <typename T>
class Queue {
	public:
		Node<T>* first;
		Node<T>* last;
		void enqueue(T item) {
			Node<T>* node = new Node<T>(item);
			if (this->first == NULL) {
				this->last = node;
				first = last;
			}
			else {
				this->last->next = node;
				this->last = this->last->next;
			}
		}
		T dequeue() {
			if (this->first == NULL) throw logic_error("dequeue empty queue");;
			T firstData = this->first->data;
			this->first = this->first->next;
			return firstData;
		}
};

int main() {
	Stack<int>* s1 = new Stack<int>();
	s1->push(1);
	s1->push(2);
	s1->push(3);
	s1->push(4);
	cout << s1->peek() << endl; s1->pop();
	cout << s1->peek() << endl; s1->pop();
	cout << s1->peek() << endl; s1->pop();
	cout << s1->peek() << endl; s1->pop();
	cout << endl;

	Queue<int>* q1 = new Queue<int>();
	q1->enqueue(1);
	q1->enqueue(2);
	q1->enqueue(3);
	q1->enqueue(4);
	cout << q1->dequeue() << endl;
	cout << q1->dequeue() << endl;
	cout << q1->dequeue() << endl;
	cout << q1->dequeue() << endl;
	cout << endl;
}