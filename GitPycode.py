#*************************************************************************
# Author: Praveen Kumar Neelakantan                                      *
# Date: 2022-03-10                                                       *
# Purpose: This file is a sample piece of code to use in GIT             *  
#                                                                        *
#                                                                        *
#                                                                        *
#                                                                        *
#*************************************************************************

from random import shuffle
s = "LOTUS"
l = []
r = ""
for item in s:
    l.append(item)
shuffle(l)
for element in l:
    r+=element
print(r)