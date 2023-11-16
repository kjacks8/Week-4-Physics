import math

#question 1
q1radians =46*(math.pi/180) #edit the 46
print ("deg to rads is: ", q1radians)
q1radtorevs = (17)*((1)/(2*math.pi)) #edit the 17
print ("Rad to revs:",q1radtorevs)
q1rpmtorad = (78)*(1/60)*(2*math.pi/1) #edit the 78
print("Rpm to rads: ", q1rpmtorad)
print("")

print ("Question 2")
print ("A centrifuge in a medical laboratory rotates at an angular speed of 3,750 rev/min. When switched off, it rotates through 48.0 revolutions before coming to rest. Find the constant angular acceleration (in rad/s2) of the centrifuge.")
ansp = 3750 # change this number
rev = 48 # change this number
w=(3750)*(1/60)*(2*math.pi)
print (w)

b= (rev)*(2*math.pi)
print (b)
answer = ((0-w**2)/(2*b))
print ("")
print ("The answer is" , round(answer))

print("")

#QUESTION 3
#The diameters of the main rotor and tail rotor of a single-engine helicopter are 7.64 m and 1.00 m, respectively. The respective rotational speeds are 457 rev/min and 4,120 rev/min. Calculate the speeds of the tips of both rotors.
print ("Question 3 Rotor tips")
MR=7.64 #edit this number
TR =1.00 #edit this number
MRS=457 #edit this number
TRS=4120  #edit this number
MRT= (3.84)*(MRS)*(2*math.pi)*(1/60)
print ("Main rotor tips =", MRT)

TRT= (0.505)*(TRS)*(2*math.pi)*(1/60)
print ("Tail rotor tips =", TRT)

VMR=(MRT)*(1/343)

VTR=(TRT)*(1/343)

print ("vMain Rotor =", VMR)
print("vTail Rotor =",VTR)

print("")

#Question 4
#It has been suggested that rotating cylinders about 18.0 mi long and 4.99 mi in diameter be placed in space and used as colonies. What angular speed must such a cylinder have so that the centripetal acceleration at its surface equals the free-fall acceleration on Earth?
print("Question 4.")
longInMiles = 16.5 #edit this number
diameterInMiles = 4.10  #edit this number
diameterinMeters = diameterInMiles*(1609/1) 
g = 9.81

radius = diameterinMeters/2

AC = math.sqrt (g/radius)
print ("Diameter in meters is ", diameterinMeters)
print ("Radius = ",radius)
print("")
print ("So, The answer is:",AC)
print("")

print ("Question 5: Human centrifuges are used to train military pilots and astronauts in preparation for high-g maneuvers. A trained, fit person wearing a g-suit can withstand accelerations up to about 9g (88.2 m/s2) without losing consciousness.")
a9g=88.2**2
hr=3.98 #edit this number
g=9.81
w= (math.sqrt (9 * g /3.98))#change this number (the last one)
print("")
print ("Answer A is:" , (w))

lsp= w*hr

print ("Answer B is: " , lsp)
print("")
#QUESTION 7  An old millstone, used for grinding grain in a gristmill, is a solid cylindrical wheel that can rotate about its central axle with negligible friction. The radius of the wheel is 0.330 m. A constant tangential force of 300 N applied to its edge causes the wheel to have an angular acceleration of 0.900 rad/s2.
print ("Question 7.")
TF = 300 #edit this number
RW = 0.330   #edit this number
AA = 0.900   #edit this number

answer = (TF *RW /AA)

print ("Answer A=" , answer)

m= ((2 * answer) / (RW**2))
print ("Answer B=" ,m)

seconds = 6.00 
w= 0+(AA)*(seconds) 
print ("Answer c =",w)
print("")

#A mechanic changing the spark plugs in a car notes that the instruction manual calls for a torque with a magnitude of 39 N · m. If the mechanic grasps the wrench as shown in the figure below, determine the magnitude (in N) of the force she must exert on the wrench.
print ("Question 8.")
torque = 39   #edit this number
distance = 0.30   #edit this number
angle = 60   #edit this number

force = torque / (distance * math.sin(math.radians(angle)))

print("The answer to question 8 is: Force:", force, "N")