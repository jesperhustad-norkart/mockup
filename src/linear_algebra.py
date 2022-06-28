
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math


def test():
    print("hello world!")


size = 2000
line = np.zeros(size)

def pdf(width = 3):
    mu = 0
    variance = width
    sigma = math.sqrt(variance)
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, math.ceil(sigma*6))
    y = stats.norm.pdf(x, mu, sigma)
    return y

def linear(b, x):
    return b - x * np.arange(b/x)


def addToLine(points, offset = 0, multiply = 1):
    for i, n in enumerate(points):
        if(offset + i <= points.size):
            line[offset + i] += n * multiply




def generate_chimney_use():
    line = np.zeros(size)
    addToLine(pdf(), 1)
    addToLine(pdf(6), 5)
    addToLine(pdf(20), 1000,100)
    addToLine(linear(0.5,0.025))
    return line

# add linear function to line


# print(np.zeros(size))

# print(np.random.choice(np.arange(5), 1, p=[1, 0, 0, 0.3, 0.7]))

# plt.plot(np.linspace(0, size, size), line)
# plt.show()

# NORMALIZE ARRAY
# norm = np.linalg.norm(an_array)
# normal_array = an_array/norm

def uniform_proposal(x, delta=2.0):
    return np.random.uniform(x - delta, x + delta)

def metropolis_sampler(p, nsamples, proposal=uniform_proposal):
    x = 1 # start somewhere

    for i in range(nsamples):
        trial = proposal(x) # random neighbour from the proposal distribution
        acceptance = p(trial)/p(x)

        # accept the move conditionally
        if np.random.uniform() < acceptance:
            x = trial

        yield x

def gaussian(x, mu, sigma):
    return 1./sigma/np.sqrt(2*np.pi)*np.exp(-((x-mu)**2)/2./sigma/sigma)

p = lambda x: gaussian(x, 1, 0.3) + gaussian(x, -1, 0.1) + gaussian(x, 3, 0.2)
# samples = list(metropolis_sampler(p, 100000))