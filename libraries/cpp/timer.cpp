#include "timer.h"

void Timer::start() {
  this->start_var = std::chrono::high_resolution_clock::now();
}

float Timer::get() {
  std::chrono::duration<float> duration = std::chrono::high_resolution_clock::now() - this->start_var;
  return duration.count();
}
