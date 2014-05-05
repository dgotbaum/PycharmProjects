#August Olsen and Andrew Winslow
#4/6/13
#We have adhered to the honor code

import soundwave
import sys
Major = [2,2,1,2,2,2,1]
Minor = [2,1,2,2,1,2,2]
Blues = [3,2,1,1,3,2]
AUG = 1.05946
dur = 0.3
def main():
    scaleIndex = sys.argv[2]
    halftone = eval(sys.argv[1])
    intervals = []
    if scaleIndex == 'M':
        intervals = Major
    elif scaleIndex == 'N':
        intervals = Minor
    elif scaleIndex == 'B':
        intervals = Blues
    else:
        print(scaleIndex , " not a valid scale option.")
        sys.exit()
    music = soundwave.Soundwave()
    music.concat(soundwave.Soundwave(halftone,dur))
    for number in intervals:
        print(intervals)
        halftone = halftone + number
        music.concat(soundwave.Soundwave(halftone,dur))
    music.play()
main()