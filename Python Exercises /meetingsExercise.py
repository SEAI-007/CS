"""
Youre given a list of meeting intervals, where each interval is defined by a start time and an end time 
(intervals[i] = [startᵢ, endᵢ]). 
Determine whether its possible for one person to attend every meeting without any overlaps.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
Constraints:

0 <= intervals.length <= 10^4
Each interval has exactly two elements (intervals[i].length == 2)
0 <= startᵢ < endᵢ <= 10^6
"""


# find highest number in intervals
# create a list with that many places
# try to fill out the places in the list with the given time ranges
# if it doesnt collide all good!

#OR

#start with the first interval, if the next intervals start or end is NOT inbetween - all good

#Input: intervals = [[0,30],[5,10],[15,20]]
def meeting(intervals):
    for interval in intervals:
        # interval = [7,10]
        start = interval[0] # 7
        end = interval[1] # 10
        for i in range (1,len(intervals)):
            if (intervals[i][0] >= start or intervals[i][0] <= end) and (intervals[i][1] >= start or intervals[i][1] <= end):
                print("Meeting not possible")
                return False
            else:
                continue

intervals = [[0,30],[5,10],[15,20]]
meeting(intervals)

