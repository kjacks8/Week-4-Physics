#Question 4
#It has been suggested that rotating cylinders about 18.0 mi long and 4.99 mi in diameter be placed in space and used as colonies. What angular speed must such a cylinder have so that the centripetal acceleration at its surface equals the free-fall acceleration on Earth?
import math
print("Question 4.")
longInMiles = 16.5 #edit this number
diameterInMiles = 4.10  #edit this number
diameterinMeters = diameterInMiles*(1609/1) 
g = 9.81

radius = diameterinMeters/2

AC = math.sqrt (g/radius)
print ("Diameter in meters is ", diameterinMeters)
print ("Radius = ",radius)
print ("The answer is:",AC)
print("")