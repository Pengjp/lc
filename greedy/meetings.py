meetings1 = [[1,10],[11,20],[10,11]]
meetings2 = [[6,12],[7,9],[9,9]]
def arrangeMeeting(meetings):
    meetings = sorted(meetings,key=lambda x:(x[-1],x[0]))
    # print(meetings)
    ans = 0
    cur_time = 0
    for i in meetings:
        if cur_time <= i[0]:
            cur_time = i[1]
            ans += 1
    print(ans)

arrangeMeeting(meetings1)
arrangeMeeting(meetings2)
