import math
print ("Question 2")
print ("A centrifuge in a medical laboratory rotates at an angular speed of 3,750 rev/min. When switched off, it rotates through 48.0 revolutions before coming to rest. Find the constant angular acceleration (in rad/s2) of the centrifuge.")
ansp = 3750 # change this number
rev = 48 # change this number
w=(3750)*(1/60)*(2*math.pi)
print (w)

b= (rev)*(2*math.pi)
print (b)
answer = ((0-w**2)/(2*b))
print ("The answer is" , round(answer))