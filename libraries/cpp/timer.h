#pragma once
#include <chrono>

class Timer {
	private:
	std::chrono::time_point<std::chrono::steady_clock> start_var;
	public:
	  void start();
	  float get();
};
