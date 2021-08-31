#include "timer.h"

Timer::Timer() {
	this->start_var = std::chrono::system_clock::now();
}
void Timer::start() {
	this->start_var = std::chrono::system_clock::now();
}
double Timer::get() {
	return std::chrono::duration<double>(std::chrono::system_clock::now() - this->start_var).count();
}
