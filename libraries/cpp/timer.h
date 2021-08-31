#include <chrono>

class Timer {
	private:
	  std::__ccr1::chrono::system_clock::time_point start_var = std::chrono::system_clock::now();
	public:
	  Timer();
	  void start();
	  double get();
};
