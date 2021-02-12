//======================================================================
// Github: https://github.com/thjsimmons
//======================================================================

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


