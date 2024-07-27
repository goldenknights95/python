# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:04:46 2024

@author: rajau
"""

"""
problem statement
John has a list of his monthly expenses from last year:


monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12,
                    1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
He wants to know his average expenses for each semester. Using a for loop, 
calculate John’s average expenses for the first semester (January to June) and
 the second semester (July to December).
 
"""

sem_1=0
sem_2=0
exp1=0
exp2=0

monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12,
                    1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
for i in range(6):
    monthly_spending[i]+=sem_1
      
    
        
        
for i in range(6,12):
     monthly_spending[i]+=sem_2
     

      
        

exp1=sem_1/6
exp2=sem_2/6

print(exp1)
print(exp2)       