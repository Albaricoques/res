/*
D. Sum Problem
time limit per test: 3 seconds ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

Implement a data structure that supports the set of S integers with which the following operations are allowed:
	 — add the number i to the set S (if it is already there, the set does not change);
	 — output the sum of all elements x from S that satisfy the inequality l ≤ x ≤ r. 

Input
Initially, the set S is empty. The first line of the input file contains n — the number of operations (1 ≤ n ≤ 300 000). The next n lines contain operations. Each operation has the form either "+ i" or "? l r". Operation "? l r" sets the query to .
If the operation "+ i" is in the input file at the beginning or after another operation "+", then it defines the operation . If it goes after the query "?", and the result of this query was y, then the operation is performed.
In all queries and adding operations, the parameters are in the range from 0 to 109.

Output
For each request print one number — the response to the request.

Example
Input
6
+ 1
+ 3
+ 3
? 2 4
+ 1
? 2 4
+ 1
+ 2
? 2 4
0

Output
3
7
9
*/


#include <iostream>
#include <memory>

struct Node {
  long val; // max 10**9
  int priority;
  long long sum; 
  std::shared_ptr<Node> left;
  std::shared_ptr<Node> right;
  
  Node(long value) : val(value), priority(rand()), sum(value), left(NULL), right(NULL) { };
};

// Returns the sum of a node owned by t if it is not empty and 0 otherwise.
long long getSum(std::shared_ptr<Node> t) {
  if (!t)
    return 0;
  return t->sum;
}

// Updates a node owned by t if it is not empty.
void update(std::shared_ptr<Node> t) {
  if (t) {
    t->sum = t->val + getSum(t->left) + getSum(t->right);
  }
}

// Splits a subtree rooted in t by value. 
std::pair<std::shared_ptr<Node>, std::shared_ptr<Node>> split(std::shared_ptr<Node> t, long value) {
  //case of node==null
  if (!t)
    return std::make_pair(std::shared_ptr<Node>(), std::shared_ptr<Node>());
  
  //set a type of output variable
  std::pair<std::shared_ptr<Node>, std::shared_ptr<Node>> res; 

  if (t->val > value) {
    auto ret = split(t->left, value); // auto - type is deduced from initializer. (in the type specifier of a variable: auto x = expr;. ) 
    t->left = ret.second;
    res = std::make_pair(ret.first, t); 
  } else {
    auto ret = split(t->right,value); 
    t->right = ret.first;
    res = std::make_pair(t, ret.second); 
  }
  update(t);
  return res;
}

// Merges the nodes owned by L and R and returns the result.
std::shared_ptr<Node> merge(std::shared_ptr<Node> L, std::shared_ptr<Node> R) {
  if (!L || !R)
    return L ? L : R;
  if (L->priority > R->priority) {
    L->right = merge(L->right, R);
    update(L);
    return L;
  } else {
    R->left = merge(L, R->left);
    update(R);
    return R;
  }
}

bool search(std::shared_ptr<Node>& root, long key) { 
    // Base Cases: root is null or key is present at root 
    if (!root)
        return false;
    if (root->val == key) 
       return true; 
      
    // Key is greater than root's key 
    if (root->val < key) 
       return search(root->right, key); 
   
    // Key is smaller than root's key 
    return search(root->left, key); 
} 

// Adds a new element of a value newValue.
void addElement(std::shared_ptr<Node>& root, long newValue) { 
  if (search(root, newValue)) {
    return;
  }
  auto parts = split(root, newValue); 
  std::shared_ptr<Node> newNode = std::make_shared<Node>(newValue);
  auto temp = merge(parts.first, newNode);
  root = merge(temp, parts.second);
}


long long countSum(std::shared_ptr<Node>& root, long l, long r) {
  if (!root) {
    return 0;
  }
  auto parts = split(root, l-1);

  if (!parts.second) { 
    root = merge(parts.first, parts.second);
    return 0;
  };

  auto parts2 = split(parts.second, r);

  if (!parts2.first){
    parts.second = merge(parts2.first, parts2.second);
    root = merge(parts.first, parts.second);
    return 0;
  }
  
  long long ans;
  ans = parts2.first->sum;
  parts.second = merge(parts2.first, parts2.second);
  root = merge(parts.first, parts.second);
  return ans;
}


int main() {
  std::shared_ptr<Node> root;
  long n;
  long l,r;
  long long y;
  char s;
  y = 0;
  scanf("%li", &n);
  for (long i = 0; i < n; i++) {

    std::cin >> s;
    if (s == '+') {
      scanf("%li", &l);
      l = (l + y) % 1000000000;
      addElement(root, l);
    } else {
      scanf("%li %li", &l, &r);
      y = countSum(root, l, r);
      printf("%lli\n", y);
      continue;
    }
    y = 0;  

  }
}
