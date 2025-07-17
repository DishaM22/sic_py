import numpy as np
spendings=np.array([10,50,101,204,30,95,500])
#we use .where() to find the indices where the condition is met

high_spendings=np.where(spendings>100)
print(high_spendings)
# Op: Indices where the values are greater than 100