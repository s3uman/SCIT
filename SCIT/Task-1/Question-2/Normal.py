import numpy as np
import matplotlib.pyplot as plt

for x in range(1,4):
    mu, sigma = 0, 0.1
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
    np.savetxt("Normal dataset"+str(x),s)
    plt.xlabel('Data')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normal Distribution')
    plt.show()
    #plt.savefig('Mgraphs/Normal/graph'+str(i)+'.png')
