//======================================================================
// Github: https://github.com/thjsimmons
//======================================================================


#ifndef EYELIKE_PROJECT_TIMER_H
#define EYELIKE_PROJECT_TIMER_H

#include <chrono>
#include <iostream>

class Timer {

public:
   void Start();
   void Stop();

private:
   std::chrono::time_point<std::chrono::system_clock> m_start;
   std::chrono::time_point<std::chrono::system_clock> m_stop;

};

#endif
