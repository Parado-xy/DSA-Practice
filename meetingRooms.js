// Given an array of meeting time intervals consisting of start and end times
// [(s1,e1),(s2,e2),...] (si < ei),
//  determine if a person could attend all meetings.

// Input: intervals = [(0,30),(5,10),(15,20)]
// Output: false
// Explanation:
// (0,30), (5,10) and (0,30),(15,20) will conflict

/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals) {
    // Sort the intervals array according to start time;
    intervals.sort((intervalA, intervalB) => intervalA.start - intervalB.start);
    // Move through the array...
    // Start one interval ahead.
    for (let i = 1; i < intervals.length; i++) {
      // Check if the start time of the current interval is not less than the end time of the previous interval
      if (intervals[i].start < intervals[i - 1].end) {
        return false;
      }
    }
    return true;
  }
}
