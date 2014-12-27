#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stack>
#include <unordered_map>

using namespace std;

template<class T>
class BinaryTree;

template<class T>
class Node {
	friend class BinaryTree<T>;
	public:
		Node* left;
		Node* right;
		T data;
		int state;
		const int id;
		Node() : id(count++), left(NULL), right(NULL) {};
		Node(T mydata) : id(count++), data(mydata), left(NULL), right(NULL) {};
		~Node() {};
	protected:
		static int count;
};

template<class T>
int Node<T>::count = 0;

template<class T>
class BinaryTree {
	public:
		BinaryTree() : root(NULL) {};
		~BinaryTree() {};

		void insert(T key);
		Node<T> *search(T key);
		void destroy_tree();
		int maxDepth();
		bool isBalanced();
		bool isBalanced2();
		void printTree();
		bool search(Node<T>* a, Node<T>* b);
		Node<T>* getRoot() { return this->root; }
		Node<T>* getMin() {
			if (this->root == NULL) return NULL;
			Node<T>* cur = this->root;
			while (cur->left != NULL) cur = cur->left;
			return cur;
		}
		Node<T>* getMax() {
			if (this->root == NULL) return NULL;
			Node<T>* cur = this->root;
			while (cur->right != NULL) cur = cur->right;
			return cur;
		}

		void visulizeTree();
	private:
		void destroy_tree(Node<T>* leaf);
		void insert(T key, Node<T>* leaf);
		Node<T> *search(T key, Node<T>* leaf);
		int maxDepth(Node<T>* leaf);
		int checkDepth(Node<T>* n);
		void printTree(Node<T>* leaf);
		bool isBalanced(Node<T>* leaf);
		bool isBalanced2(Node<T>* leaf);

		Node<T> *root;
};

template<class T>
void BinaryTree<T>::insert(T key, Node<T>* leaf) {
	if (key < leaf->data) {
		if (leaf->left != NULL) insert(key, leaf->left);
		else leaf->left = new Node<T>(key);
	}
	else {
		if (leaf->right != NULL) insert(key, leaf->right);
		else leaf->right = new Node<T>(key);
	}
}

template<class T>
void BinaryTree<T>::destroy_tree(Node<T>* leaf) {
	if (leaf != NULL) {
		if (leaf->left != NULL) destroy_tree(leaf->left);
		if (leaf->right != NULL) destroy_tree(leaf->right);
		delete leaf;
	}
	return;
}

template<class T>
void BinaryTree<T>::insert(T key) {
	if (this->root != NULL) insert(key, this->root);
	else this->root = new Node<T>(key);
}

template<class T>
void BinaryTree<T>::destroy_tree() {
	destroy_tree(this->root);
}

template<class T>
BinaryTree<T>* createRandomTree(int num) {
	BinaryTree<T>* bt = new BinaryTree<T>();
	srand(time(NULL));
	for (int i = 0; i < num; ++i) {
		int random = rand() % 100;
		bt->insert(random);
	}
	return bt;
}

template<class T>
void BinaryTree<T>::visulizeTree() {

	stringstream ss1, ss2;

	stack<Node<T>*> nodes;
	unordered_map<int,string> map;
	nodes.push(this->root);

	while(nodes.empty() == false) {
		Node<T>* cur = nodes.top(); nodes.pop();
		map[cur->id] = "index: " + to_string(cur->id) + " | " + "value: " + to_string(cur->data) + " | " + "depth: " + to_string(this->maxDepth(cur));
		if (cur->left) ss2 << "\tnode" << cur->id << ":left -> " << "node" << cur->left->id << ";" << endl;
		if (cur->right) ss2 << "\tnode" << cur->id << ":right -> " << "node" << cur->right->id << ";" << endl;
		if (cur->left) nodes.push(cur->left);
		if (cur->right) nodes.push(cur->right);
	}

	for (int i = 0; i < this->root->count; ++i) {
		ss1 << "\tnode" << i << "[label=\"{" << map[i] << "|{<left>|<right>}}\"];" << endl;
	}

	ofstream myfile;
	myfile.open ("sample.dot");
	myfile << "digraph G{" << endl;
	myfile << "\tnode[shape=record];" << endl;
	myfile << ss1.str() << ss2.str();
	myfile << "}" << endl;
	myfile.close();
	system("dot -Tjpeg sample.dot -o sample.jpg");
	system("open sample.jpg");
	return;
}

// in order
template<class T>
void BinaryTree<T>::printTree(Node<T>* n) {
	if (n->left) printTree(n->left);
	cout << n->data << ' ';
	if (n->right) printTree(n->right);
}

template<class T>
void BinaryTree<T>::printTree() {
	printTree(this->root);
	return;
}

// 4.1 Implement a function to check if a binary tree is balanced. For the purposes of
// this question, a balanced tree is defined to be a tree such that the heights of the
// two subtrees of any node never differ by more than one.

template<class T>
int BinaryTree<T>::maxDepth(Node<T>* n) {
	if (n == NULL) return 0;
	return fmax(maxDepth(n->left), maxDepth(n->right)) + 1;
}

template<class T>
int BinaryTree<T>::checkDepth(Node<T>* n) {
	if (n == NULL) return 0;

	int lDepth = checkDepth(n->left);
	if (lDepth == -1) return -1;

	int rDepth = checkDepth(n->right);
	if (rDepth == -1) return -1;

	if (abs(lDepth - rDepth) > 1) { return -1; }
	else return fmax(lDepth, rDepth) + 1;
}

template<class T>
int BinaryTree<T>::maxDepth() {
	return maxDepth(this->root);
}

template<class T>
bool BinaryTree<T>::isBalanced(Node<T> * n) {
	if (n != NULL) {
		if (abs(maxDepth(n->left) - maxDepth(n->right)) > 1) return false;
		else return isBalanced(n->left) && isBalanced(n->right);
	}
	return true;
}

template<class T>
bool BinaryTree<T>::isBalanced() {
	return isBalanced(this->root);
}

template<class T>
bool BinaryTree<T>::isBalanced2(Node<T> * n) {
	if (checkDepth(n) == -1) return false;
	return true;
}

template<class T>
bool BinaryTree<T>::isBalanced2() {
	return isBalanced2(this->root);
}

// 4.2 Given a directed graph, design an algorithm to find out whether there is a route
// between two nodes.

template<class T>
bool BinaryTree<T>::search(Node<T>* a, Node<T>* b) {
	if (a == NULL || b == NULL) return false;
	if (a->id == b->id) return true;
	return search(a->left, b) || search(a->right, b);
};

template<class T>
Node<T>* randomWalk(Node<T>* cur, int steps) {
	if (cur == NULL) return cur;
	srand(time(NULL));
	for (int i = 0; i < steps; i++) {
		int random = rand() % 2;

		if (cur->left != NULL && cur->right != NULL) {
			if (random == 0) cur = cur->left;
			else cur = cur->right;
		}
		else if (cur->left != NULL) cur = cur->left;
		else if (cur->right != NULL) cur = cur->right;
		else return cur;
	}
	return cur;
}

int main() {
	BinaryTree<int>* bt = createRandomTree<int>(100);
	bt->visulizeTree();
	cout << bt->maxDepth() << endl;
	cout << bt->isBalanced() << endl;
	cout << bt->isBalanced2() << endl;
	bt->printTree(); cout << endl;

	Node<int>* btRoot = bt->getRoot();

	Node<int>* a = randomWalk<int>(btRoot, 2);
	Node<int>* b = randomWalk<int>(btRoot, 5);
	cout << "random node a " << a->id << " " << a->data << endl;
	cout << "random node b " << b->id << " " << b->data << endl;
	cout << "path from a to b: " << bt->search(a, b) << endl;
	cout << endl;

	Node<int>* c = bt->getMin();
	Node<int>* d = bt->getMax();
	cout << "min node c " << c->id << " " << c->data << endl;
	cout << "max node d " << d->id << " " << d->data << endl;
	cout << "path from c to d: " << bt->search(c, d) << endl;
	cout << endl;


	bt->destroy_tree();
}
