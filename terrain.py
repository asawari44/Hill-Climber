import numpy as np
import matplotlib.pyplot as plt

def get_basic_terrain(size=100):
    x = np.arange(0, size, 1)

    noise = np.random.normal(scale=3, size=[1, size])

    terrain = x + noise

    terrain.shape[1]

    return terrain

def get_sine_terrain(size=100):
    Fs = 100
    f = 2
    sample = 100
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    
    return y.reshape(1,size)

def get_basic_terrain_descending(size=100):
    x = np.arange( size,0, -1)

    noise = np.random.normal(scale=3, size=[1, size])

    terrain = x + noise

    terrain.shape[1]

    return terrain