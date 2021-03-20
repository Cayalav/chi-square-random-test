from scipy.stats.distributions import chi2
#import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

#Chi observado, sumatoria
def chiobserve(random_nums):
  n = len(random_nums)
  r = max(random_nums) - min(random_nums)
  k = np.ceil(sqrt(n))
  a = r/k
  chio=0
  countei = int(n/k) 
  down = min(random_nums)
  countoiarr = []
  for x in range(int(k)):
    up = down + a
    countoi = 0  
    for y in range(n):
      if(down <= random_nums[y] <= up):
        countoi = countoi+1
    countoiarr.append(countoi)  
    down = up
    chio= chio + (pow(countoi-countei,2)/countei)
  print("Valor observado:")  
  print(chio)
  print("\n")
  #plt.hist(countoiarr)  
  #plt.show()
  return chio


#Chi teorico, libreria python
def chiteoric(random_nums): #N-1
  chit = chi2.ppf(0.95, len(random_nums)-1)
  print("Valor teorico:")  
  print(chit)
  print("\n")   
  return chit

#Llamado general
def goodnes_of_fit(random_nums): #N-1
  if (chiobserve(random_nums) <= chiteoric(random_nums)):
    print("Es uniforme") 
  else:
    print("No es uniforme")   
  print("----------------------")   
  print("\n") 
  print("\n") 

arr1 = [0.1791, 0.1010, 0.8558, 0.7294, 0.6464, 0.2891, 0.8648, 0.8378, 0.8910, 0.7127, 0.3354, 0.3856, 0.9458, 0.2870, 0.2691, 0.6123, 0.4133, 0.8251, 0.1766, 0.7554]

arr2 = [ 1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,5,6,7,8,10,2,9]

arr3 = np.random.rand(300)

goodnes_of_fit(arr1)
goodnes_of_fit(arr2)
goodnes_of_fit(arr3)


