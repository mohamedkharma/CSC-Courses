/*
 * CSc103 Project 2: prime numbers.
 * See readme.html for details.
 */

#include <iostream>
using std::cin;
using std::cout;
using std::endl;
#include <cmath>

int main() {
	unsigned long n;
	while (cin >> n)
		{
			int isPrime = 0;
			if (n <= 1) {
					isPrime = 1;
			}
			for (int i=2; i<=sqrt(n); i++)
			{
					if (n%i == 0) {
					isPrime = 1;
					break;
					}
			}
		if  (isPrime == 1) {
			cout << "0 \n";
		}else{
			cout <<"1 \n";
	  }
	}
}
