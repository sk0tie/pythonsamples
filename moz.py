#!/usr/bin/python

# Scott Wilcox
# scottleewilcox@gmail.com
# (206) 234-2799
#
# Moz Interview Coding Questions

#####################
# Provided Moz Code #
#####################

#for i in range(0, 8):
#  sum = 0
#  power = 0
#  print 2 ** power
#  sum = 2 ** power
#print sum

##################
# Corrected Code #
##################

#sum = 0
#for i in range(0, 8):
#    power = i
#    print(2 ** power)
#    sum = sum + 2 ** power
#print(sum)

###############
# Leaner Code #
###############

sum = 0
for i in range(0, 8):
    print(2 ** i)
    sum = sum + 2 ** i
print(sum)

# End of example.

############################################
# Code To Print Two Text Files Interleaved #
############################################

# To use, create two files, file1.txt and file2.txt and put lines of text in them.

# Get a new line to separate from previous example code result.
print()

# Initialize a few lists to hold our data.
file1list = list()
file2list = list()

# Open files and read them into arrays that we can work with.

with open('file1.txt') as file1:
    file1list = file1.readlines()

with open('file2.txt') as file2:
    file2list = file2.readlines()

# !! I realized using zips only works if the lists are the same length.
# Left in the commented out the code below to show what thought I started with.
#
# Import the chain/zip libraries from itertools.
#
#from itertools import chain
#
#interleave = list(chain.from_iterable(zip(file1list, file2list)))
#
#for x in interleave:
#    print(x.rstrip())

# Instead of the above, we can use try blocks to attempt to read from an array item, and handle errors if it doesn't exist.

# Get the count of the longest array.
longestcount = max(len(file1list), len(file2list))

# Itterate through the both arrays at the same time, handling errors if one does not have as many elements.
for x in range(0,longestcount):
    try:
        print(file1list[x].rstrip()) # Reading the files into an array appended new lines, strip this off while printing.
    except IndexError: 
        pass # If we get an error, don't worry about it, move on through the loop until we reach our count.
    try:
        print(file2list[x].rstrip())
    except IndexError:
        pass
        
# End of example.


#############################
# Extract Domains from URLs #
#############################

# Had a bit of trouble with this, different versions of the python regex library behave differently, I just picked one that worked.
# Admittedly; I'm not super good at regex. :)

# Import python's regex library.
import re

# Open file.
with open('urls.txt') as urls:
    # Loop through the urls.
    for url in urls:
        # Search with regex, building a group the match anything between one forward slash, and a second backslash, query or end line.
        # ?<=/ -- First forward slash.
        # .*? -- Anything.
        # ?=/|\?|\\z) -- Trailing forward slash, query or end line. (Escape that backslash for \z !! :)
        result = re.search('(?<=/)(.*?)(?=/|\?|\\\z)', url)
        if result:
            # Print first result from group 1.
            print(result.group(1))

# End of example.
