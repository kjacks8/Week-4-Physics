import math
#question 5
print ("Human centrifuges are used to train military pilots and astronauts in preparation for high-g maneuvers. A trained, fit person wearing a g-suit can withstand accelerations up to about 9g (88.2 m/s2) without losing consciousness.")
a9g=88.2**2
hr=3.98 #edit this number
g=9.81
w= (math.sqrt (9 * g /3.98))#change this number (the last one)
print ("Answer A is:" , (w))

lsp= w*hr

print ("Answer B is: " , lsp)
