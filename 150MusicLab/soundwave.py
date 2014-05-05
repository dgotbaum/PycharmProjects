# August Olsen and Andrew Winslow
# 4/6/13
# We have adhered to the honor code
#
import math
import audio

class Soundwave:
    
    def __init__(self, halftones=0, duration=0.0, amp=1.0, samplerate=44100):
        
        if isinstance(halftones, str) == True:
            
            
            self.samples = audio.read_file(halftones)
            #                 ^as this delivers a list of samples
            self.halftones = halftones
            duration = (len(self.samples))/41400
            self.length = duration
            # figuring out the duration based on the number of samples
            self.maxvol = amp
            self.samplerate = samplerate
            
            
        else:   
            self.halftones = halftones
            self.length = duration
            self.maxvol = amp
            self.samplerate = samplerate
            
            self.samples = [0]*(int(self.length*self.samplerate))
            
            freq = 440*(2**((halftones+3)/12))
            
            for t in range(len(self.samples)):
                self.samples[t] = amp*math.sin(2*math.pi*freq*t/samplerate)
        
    def play(self):
        audio.play(self.samples)

    def concat(self, s2):
        self.samples.extend(s2.samples)
        self.length = self.length + s2.length
        self.maxvol = self.maxvol + s2.maxvol
    
        
    def plus(self, s2):
        
        s = Soundwave()
        
        combo = [0]*(int(self.length*self.samplerate))
        
        if len(self.samples) >= len(s2.samples):
            for t in range(len(s2.samples)):
                combo[t] = self.samples[t] + s2.samples[t]
            combo.append(self.samples[(len(self.samples)-len(s2.samples)):])
        else:
            for t in range(len(self.samples)):
                combo[t] = self.samples[t] + s2.samples[t]
            combo.append(s2.samples[(len(s2.samples)-len(self.samples)):])
                
        
        if (self.length > s2.length):
            s.length = self.length
        else:
            s.length = s2.length
        
        if (self.maxvol > s2.maxvol):
            s.maxvol = self.maxvol
        else:
            s.maxvol = s2.maxvol
            
        s.samplerate = 41400
        
        return s
        