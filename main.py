##==========[PHOTRON:START]==========##

  #----------importing time modules----------#
import time

  #----------assigning variables----------#
secs = 10 * int(input('Enter seconds: '))

  #----------creating loop----------#
for part_sec in range(secs-1,-1,-1):
  time.sleep(0.1)
  #----------calculations----------#
  seconds = part_sec // 10
  format_min = seconds // 60
  format_sec = seconds % 60
  format_milli = (part_sec % 10) * 100
  #----------print statement for the loop----------#
  print(f"\t{format_min:02d}m:{format_sec:02d}s:{format_milli}ms\r", end='')
  
  #----------final print statement----------#
print('\n\nTime\'s up!')

##==========[PHOTRON:END]==========##
