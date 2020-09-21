import numpy as np

def generate_bimodal(mu1=50, mu2=100, std1=30, std2=40, size=1000):
    dist1 = np.random.normal(mu1, std1, size=size//2)
    dist2 = np.random.normal(mu2, std2, size=size//2)
    return np.concatenate([dist1, dist2])
    
