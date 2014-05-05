#
#
#
#
#add concatinations


import sys

import soundwave

Major =

if sys.args[2] == M:
    #do major
    interval = [2,2,1,2,2,2,1]
    l = []
    prev = sys.args[1]
    for i in range(9):
        if i == 1:
            l.append(sysarg[1])
        else:
            l.append(prev*(1.05946**i))
        
        #just for reference
        #s1 = soundwave.Soundwave(sys.args[1])
        #s2 = soundwave.Soundwave((s1)*(1.05946**2))
        #s3 = soundwave.Soundwave((sys.args[1])*(1.05946**4))
        #s4 = soundwave.Soundwave((sys.args[1])*(1.05946**5))
        #s5 = soundwave.Soundwave((sys.args[1])*(1.05946**7))
        #s6 = soundwave.Soundwave((sys.args[1])*(1.05946**9))
        #s7 = soundwave.Soundwave((sys.args[1])*(1.05946**11))
        #s8 = soundwave.Soundwave((sys.args[1])*(1.05946**12))
    
    #use play at the end
elif sys.args[2] == N:
    #do minor
    interval = [2,1,2,2,1,2,2]
    l = []
    prev = sys.args[1]
    for i in range(9):
        if i == 1:
            l.append(sysarg[1])
        else:
            l.append(prev*(1.05946**i))
elif sys.args[2] == B:
    #do blues
    interval = [3,2,1,1,3,2]
    l = []
    prev = sys.args[1]
    for i in range(9):
        if i == 1:
            l.append(sysarg[1])
        else:
            l.append(prev*(1.05946**i))
    
    
#figuring out where to start
halftones = sys.args[1]


intervals = [[2,2,1,2,2,2,1], [2,1,2,2,1,2,2], [3,2,1,1,3,2]]

#decide which halfstep to start on
    #number should be distance above or below middle C (440) in halftones
#decide whether scale is major, minor, or blues
    #use concat funciton to string the notes together into one soundwave