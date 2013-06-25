# Import the file

from sys import argv

script, filename = argv

# Opening the file, reading the file 
# Assign the read file to a variable

restaurants_scores = open(filename)


rest_dict = {}

for line in restaurants_scores:

	restaurant = line.strip().split(':')
	rest_dict[restaurant[0]] = restaurant[1]

print rest_dict

sorted_dict = sorted(rest_dict)


for rest in sorted_dict:
	print rest + ":" + rest_dict[rest]

# for name, rating in sorted_dict.iteritems(): #for the dictionary we have created above
	# print "Restaurant %s is rated at %s" % (name, rating)


















