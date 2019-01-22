#include<iostream>
#include<stdlib.h>
using namespace std;

#define MAX_SIZE 10	// the length of the array

// sequential struct
struct sq_list {
	int* sq_base;
	int len;
};

// list of methods
sq_list init();
void add(int data, sq_list& list, int pos=-1);
int max_size();
void print_list(sq_list list);
void remove(sq_list& list, int pos=-1);



int main() {
	// init sequential list
	sq_list list = init();
	
	// add element
	add(8, list);
	add(9, list);
	add(9, list);
	add(9, list);
	add(10, list, 1);	
	remove(list, 1);
	// print the result
	print_list(list);
	system("pause");
	return 0;
}

// use -1 as the value
sq_list init() {
	sq_list list;
	list.sq_base = (int*) malloc (sizeof(int) * MAX_SIZE);
	list.len = 0;
	return list;
}

// add an element to a sequential list
void add(int data, sq_list& list, int pos) {
	// when the list is full
	if (list.len == MAX_SIZE) {
		cout << "the list is full" << endl;
		return;
	}
	// not give the insert position
	if (pos == -1) {
		pos = list.len + 1;
	}
	// if position is larger than the len
	if (list.len + 1 < pos || pos < 1) {
		cout << "please input a correct position: (1 ~ " << list.len + 1<< ")." <<endl;
		return;
	}
	
	int i;
	// add new element
	if (list.len == 0) {
		i = 0;
	} else {
		i = list.len - 1;
	}
	for (; i >= pos - 1; i--) {
		list.sq_base[i + 1] = list.sq_base[i];
	}
	list.sq_base[pos-1] = data;
	list.len++;
	return;
}

// remove an element to the list
void remove(sq_list& list, int pos) {
	if (list.len == 0) {
		cout << "There is no element in the list" << endl;
		return;  
	} 
	
	if (pos == -1) {
		pos = list.len;
	}
	
	if (pos < 1 || pos > list.len) {
		cout << "Please input a correct position: ( 1 ~ " << list.len << " )" << endl;
		return;
	}
	
	// remove
	for (int i = pos - 1; i < list.len - 1; i++) {
		list.sq_base[i] = list.sq_base[i+1];	
	} 
	// free(&(list.sq_base[list.len-1]));
	list.len--;
	
}


// max of the array
int max_size() {
	return MAX_SIZE;
}

// print sequential list
void print_list(sq_list list) {
	int len = list.len;
	for (int i = 0; i < len; i++) {
		cout << list.sq_base[i] << " ";
	}
	cout << endl;
}

