# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:42:58 2024

@author: rajau
"""

"""
Paul and Tina each have a list of their respective friends:

paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
Combine both lists into a single list that contains all of their friends.
 Don’t include duplicate entries in the resulting list."
"""

paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

all_friends=paul_friends+tina_friends
x=set(all_friends)
y=list(x)
print(y)