# =============
# Approch 1:

import numpy as np

lst=[1,2,3,4,5]

ans = np.prod(lst)

print(ans)


# =============
# Approch 2:

mul1=1

for i in range(len(lst)):
    mul1= mul1 * lst[i]
    
print("-->",mul1)