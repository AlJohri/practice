# Meeting Schedules

- Source: https://amazon.interviewstreet.com/challenges/dashboard/#problem/4fd651016cd04

Given M busy-time slots of the team members in the Kindle team, can you print all the available time slots when all of them can schedule a meeting for a duration of K minutes.
The event time will be of the form HH MM (where 0 <= HH <= 23 and 0 <= MM <= 59). K will be in the form minutes.
 
Input Format:
 
M K [M number of busy time slots , K is the duration in minutes]
This is followed by M lines with 4 numbers on each line.
Each line will be of the form StartHH StartMM EndHH EndMM  [Eg: 9am-11am time slot will be given as 9 00 11 00]
An event time slot is of the form [Start Time, End Time) which means the start time is inclusive but not the end time;
So, an event of the form 10 00  11 00 => implies that the meeting starts at 10:00 and ends at 11:00. Hence, another meeting can start at 11:00.
 
Sample Input:
5 120
16 00 17 00
10 30 14 30
20 45 22 15
10 00 13 15
09 00 11 00
 
Sample Output:
00 00 09 00
17 00 20 45
 
Sample Input:
8 60
08 00 10 15
22 00 23 15
17 00 19 00
07 00 09 45
09 00 13 00
16 00 17 45
12 00 13 30
11 30 12 30
 
Sample Output:
00 00 07 00
13 30 16 00
19 00 22 00
 
Constraints :
1 <= M <= 100
 
Note: 24 00 has to be presented as 00 00.
