#!/usr/bin/env python
import motionClass
import wrapper
import arguments
import traceback
import sys
import numpy

#==================
# MAIN ENTRY POINT
#==================

if __name__ == "__main__":
        while True:
                try:
                        motionVid=motionClass.Motion()
                        arguments.arguments(motionVid)
                        wrapper.wrap(motionVid)
                        
                except ValueError, e:
                        if e.message!= 'Failed to load OpenCL runtime':
                                raise ValueError, e
        
                #reboot or exit?
                #if there were system arguments, immediately exit
                if len(sys.argv)>=2:
                        break
                ch=raw_input("Press r to reboot, press any key to exit \n")
                if ch=='r':
                        continue
                break
            


