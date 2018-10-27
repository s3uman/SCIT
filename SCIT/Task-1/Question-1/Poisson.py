import numpy as np
import matplotlib.pyplot as plt
i=1
for x in range(0,3):
    lam=6
    samples=1000
    s=np.random.poisson(lam,1000)
    np.savetxt("dataset"+str(i),s)
    count, bins, ignored = plt.hist(s, 14, density=True)
    plt.xlabel('x')
    plt.ylabel('Probability(P(X=x))')
    plt.title('Histogarm for Poisson Distribution')
    plt.show()
    plt.savefig('Mgraphs/poisson/graph'+str(i)+'.png')
    i=i+1
