#QUESTION 3
#The diameters of the main rotor and tail rotor of a single-engine helicopter are 7.64 m and 1.00 m, respectively. The respective rotational speeds are 457 rev/min and 4,120 rev/min. Calculate the speeds of the tips of both rotors.
import math
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