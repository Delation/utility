// This is supposed to calculate a list of prime numbers
// but it turns out there isn't a consistent formula for finding new ones
// so this script is broken

#include <iostream>
#include <vector>

bool check_prime(unsigned int n) {
	for (int i = 1;i < n + 1;i++) {
		if (n % i == 0) {
			if (i != 1 && i != n) {
				return false;
			}
		}
	}
	return true;
}

std::vector < unsigned int > new_prime (unsigned int n,unsigned int xrange) {
	std::vector < unsigned int > list = {};
	unsigned int x = n;
	for (int i = 0;i < xrange + 1;i++) {
		x = 6*x+1;
		list.push_back(x);
	}
	x = n;
	for (int i = 0;i < xrange + 1;i++) {
		x = 6*x-1;
		list.push_back(x);
	}
	return list;
}

double find_percentage(unsigned int xrange) {
	std::vector < bool > list = {};
	for (int i = 1;i < 41;i++) {
		unsigned int n = i*i+i+41;
		list.push_back(check_prime(n));
		for (unsigned int item: new_prime(n,xrange)) {
			list.push_back(check_prime(item));
		}
	}
	double truecount = std::count(list.begin(),list.end(),true);
	double size = list.size();
	return truecount / size * 100;
}
	
int main() {
	std::cout << "The formula gets a prime number " << find_percentage(2) << "% of the time." << std::endl;
}
