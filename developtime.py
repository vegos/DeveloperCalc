#!/usr/bin/python
#
#        Simple Developer Time / Temp Calculator
# (c)2014, Antonis Maglaras / maglaras at gmail dot com
#
import math
print
print ("DEVELOPER TIME CALCULATOR")
print ("(c)2014, Antonis Maglaras")
print

# roundtime = 1 if you want to round time
roundtime = 1

time_input = input("Enter exact time for 20C (in MM:SS): ")
InputMin, InputSec = [int(i) for i in time_input.split(':')]
OldTime = InputMin*60 + InputSec

NewTemp = input("New Temperature (in Celsius): ")
NewTime = int(OldTime)*math.exp(-0.081*(int(NewTemp)-20))
NewMin, NewSec = divmod(NewTime, 60)

if roundtime == 1:
  if NewSec > 52:
    tmpSec = 0
    NewMin += 1
  elif NewSec > 37:
    tmpSec = 45
  elif NewSec > 22:
    tmpSec = 30
  elif NewSec > 7:
    tmpSec = 15
  else:
    tmpSec = 0
  NewSec = tmpSec

print 
print ("New Time for %dC: %2d:%2d" % (int(NewTemp), int(NewMin), int(NewSec)))
print

if NewMin < 5:
  print ("Warning! Development times below 5 minutes are not recommended")
  print ("         due to the risk of uneven development!")
  print
