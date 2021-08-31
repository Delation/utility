#include <iostream>

int main() {
	int n;
	std::cout << "Your number >>> ";
	std::cin >> n;
	for (int i = 1;i < n + 1;i++) {
  		if (n % i == 0) {
    			std::cout << n;
   	 		std::cout << " is divisble by ";
    			std::cout << i << std::endl;
  		}
  	}
	return 0;
}
