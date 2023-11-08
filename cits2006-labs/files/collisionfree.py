import random
import string
import hashlib
#Collision resistance -> It's hard to find a pair of messages x1 != x2 with Hash(x1) = Hash(x2) 
avg_tried = 0

#you may need to change the number of trials to get a better average
trials = 20

for i in range(trials):
	tried = 0
	#
	# Your code goes here
    #
	print(f"run {i+1}: {tried}")
	avg_tried += tried

print(f"average: {avg_tried / trials}")
