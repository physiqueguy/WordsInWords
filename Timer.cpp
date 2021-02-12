//======================================================================
// Github: https://github.com/thjsimmons
//======================================================================


#include "Timer.h"

/* Usage:
 * -----------------------
 * Timer timer;
 *
 * timer.Start();
 *
 * *** code ***
 *
 * timer.Stop();
 * -----------------------
 *
 */

void Timer::Start(){
   m_start = std::chrono::system_clock::now();
   std::cout << "START TIMER ..." << std::endl;
}

void Timer::Stop(){

   m_stop = std::chrono::system_clock::now();
   auto duration = std::chrono::duration_cast<std::chrono::microseconds>(m_stop - m_start).count();
   std::cout << "STOP TIMER =  " << duration/1000000.0 << " seconds ";
}

