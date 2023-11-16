#QUESTION 7  An old millstone, used for grinding grain in a gristmill, is a solid cylindrical wheel that can rotate about its central axle with negligible friction. The radius of the wheel is 0.330 m. A constant tangential force of 300 N applied to its edge causes the wheel to have an angular acceleration of 0.900 rad/s2.
import math
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