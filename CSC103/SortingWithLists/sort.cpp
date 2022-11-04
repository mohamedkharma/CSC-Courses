/*
 * CSc103 Project 4: Sorting with lists
 * See readme.html for details.
 */

#include <iostream>
using std::cin;
using std::cout;
using std::endl;
#include <getopt.h> // to parse long arguments.
#include <string>
using std::string;


/* doubly linked list node: */
struct node {
	string data;
	node* prev;
	node* next;
	node(string s="", node* p=NULL, node* n=NULL) : data(s),prev(p),next(n) {}
};
/*
void printDDL(node *head){
	node *curr = head;
	while(curr != NULL) {
		if(curr != head){
			cout << "->";
		}
		cout << curr->data;
		curr = curr->next;
	}
	cout << endl;
}*/

void insert(node*& head, string line);
void reversed(node*& head);
void remove(node*& head);


int main(int argc, char *argv[]) {
	/* define long options */
	static int unique=0, reverse=0;
	static struct option long_opts[] = {
		{"unique",   no_argument,       &unique,   'u'},
		{"reverse",  no_argument,       &reverse,  'r'},
		{0,0,0,0} // this denotes the end of our options.
	};
	/* process options */
	char c; /* holds an option */
	int opt_index = 0;
	while ((c = getopt_long(argc, argv, "ur", long_opts, &opt_index)) != -1) {
		switch (c) {
			case 'u':
				unique = 1;
				break;
			case 'r':
				reverse = 1;
				break;
			case '?': /* this will catch unknown options. */
				return 1;
		}
	}


	/* NOTE: at this point, variables 'reverse' and 'unique' have been set
	 * according to the command line.  */
	/* TODO: finish writing this.  Maybe use while(getline(cin,line)) or
	 * similar to read all the lines from stdin. */
	node* head = NULL;
	string line;
	while(getline(cin,line)) {
		insert(head, line);
	}

	if(reverse == 1) {
		reversed(head);
	}

	if (unique == 1) {
		remove(head);
	}
	for (node* i = head; i != NULL; i = i->next) {
	cout << i->data << endl;
	}

	return 0;
}

	void insert(node*& head, string line) {
		//node* tail= NULL;
		//node* temp= NULL;
		//node* curr= NULL;

		if (head == NULL) {
			node* temp = new node(line);
			head = temp;
		} else {
			node* curr = head;
			node* temp = NULL;

			for (curr = head; curr != NULL && curr->data < line; curr = curr->next) {
				//curr = curr->next;
				temp = curr;
				}
				if(curr == head) {
					temp = new node;
					temp->data = line;
					temp->next = head;
					temp->next->prev = temp;
					temp->prev = NULL;
					head = temp;

				} else if (curr == NULL) {
					temp->next = new node(line,temp,NULL);
				}
				else{
					node* tail = new node(line,NULL,NULL);
					curr->prev->next = tail;
					tail->prev = curr->prev;
					tail->next = curr;
					curr->prev = tail;
				}
			}
		}


	void reversed(node*& head){
		node* temp = head;
		node* tail = NULL;
		while (temp != NULL){
			tail = temp->prev;
			temp->prev = temp->next;
			temp->next = tail;
			temp = temp->prev;
		}
			if(tail != NULL)
			head = tail->prev;

	}

	void remove(node*& head) {
		node* curr = head;
		node* p= head->next;
		while (p!= NULL){
			if(curr->data == p->data) {
				node* temp = p;
				curr->next = p->next;
				if(curr->next!= NULL)
					p->next->prev = curr;
				delete temp;
				p = p->next;
			} else {
				curr = curr->next;
				p = p->next;
			}
		}
	}


