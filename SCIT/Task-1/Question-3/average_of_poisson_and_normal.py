import numpy as np
import matplotlib.pyplot as plt
import random

mu, sigma = 0, 0.1
lam=6

for x in range(100):
    p=np.random.poisson(lam,1000)
    n = np.random.normal(mu, sigma, 1000)
    data=[]
    for m in range(100):
        rand=random.randint(0,1000)
        avg=(n[rand-1]+p[rand-1])/2
        data.append(avg)
    bins=plt.hist(data,14,density=True)
    plt.savefig('Mgraphs/Average/Average'+str(x)+'.png')
    
