import random
import string
import hashlib
#Preimage resistance -> For a given h in the output space of hash function, it's hard to find any message x with H(x) = h
#the 'h' we are checking against

#try to change the hash value to see how much harder it becomes when the length of the hash value gets longer
HASH_VALUE = 'b86d'
avg_tried = 0

#you may need to change the number of trials to get a better average
trials = 20

for i in range(trials):
	tried = 0
	while True:
		#generates random strings of length 20
		randomStr = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(16)])
		#hash the random string, using MD5	
		hash_object = hashlib.md5(randomStr.encode())
		#get a HEX string representing the hash
		hash_string = hash_object.hexdigest()
		#check first 32 bits of hash value against our 'h'
		tried += 1
		if hash_string[0:4] == HASH_VALUE:
			break
	print(f"run {i+1}: {tried}")
	avg_tried += tried

print(f"average: {avg_tried / trials}")

