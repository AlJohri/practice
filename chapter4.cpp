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
        void inOrder();

        void visulizeTree();        
    private:
        void destroy_tree(Node<T>* leaf);
        void insert(T key, Node<T>* leaf);
        Node<T> *search(T key, Node<T>* leaf);
        int maxDepth(Node<T>* leaf);
        void inOrder(Node<T>* leaf);
        bool isBalanced(Node<T>* leaf);

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
		if (cur->right) nodes.push(cur->right);
        if (cur->left) nodes.push(cur->left);
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

template<class T>
void BinaryTree<T>::inOrder(Node<T>* n) {
	cout << n->id << "(" << n->data << ")" << ' ';
	if (n->left) inOrder(n->left);
	if (n->right) inOrder(n->right);
}

template<class T>
void BinaryTree<T>::inOrder() {
	inOrder(this->root);
	return;
}

template<class T>
int BinaryTree<T>::maxDepth(Node<T>* n) {
	if (n == NULL) return 0;
	return fmax(maxDepth(n->left), maxDepth(n->right)) + 1;
}

template<class T>
int BinaryTree<T>::maxDepth() {
	return maxDepth(this->root);
}

// 4.1 Implement a function to check if a binary tree is balanced. For the purposes of
// this question, a balanced tree is defined to be a tree such that the heights of the
// two subtrees of any node never differ by more than one.

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

int main() {
	BinaryTree<int>* bt = createRandomTree<int>(100);
	bt->visulizeTree();
	cout << bt->maxDepth() << endl;
	cout << bt->isBalanced() << endl;
	bt->inOrder(); cout << endl;
	bt->destroy_tree();
}
