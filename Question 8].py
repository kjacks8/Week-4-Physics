import math
#A mechanic changing the spark plugs in a car notes that the instruction manual calls for a torque with a magnitude of 39 N · m. If the mechanic grasps the wrench as shown in the figure below, determine the magnitude (in N) of the force she must exert on the wrench.
print ("Question 8.")
torque = 39   #edit this number
distance = 0.30   #edit this number
angle = 60   #edit this number

force = torque / (distance * math.sin(math.radians(angle)))

print("The answer to question 8 is: Force:", force, "N")