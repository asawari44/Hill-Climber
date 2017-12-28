import numpy as np
import matplotlib.pyplot as plt

def get_basic_terrain(size=100):
    x = np.arange(0, size, 1)

    noise = np.random.normal(scale=3, size=[1, size])

    terrain = x + noise

    terrain.shape[1]

    return terrain

def get_sine_terrain(size=100,sample=1000,f=2):
    Fs = size
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    
    return y.reshape(1,sample)

def get_basic_terrain_descending(size=100):
    x = np.arange( size,0, -1)

    noise = np.random.normal(scale=3, size=[1, size])

    terrain = x + noise

    terrain.shape[1]

    return terrain

def terrain_complex(sample=1000):
    
    sin = get_sine_terrain(size=200,sample=1000,f=.5)

    sin1 = get_sine_terrain(size=250,sample=1000,f=.4)

    sin2 = get_sine_terrain(size=500,sample=1000,f=.6)

    terrain =  sin+sin1+sin2
    
    return terrain

def get_parabola(sample = 1000):
    
    x= np.arange(-sample/2,sample/2)
    y = 2*x*x + 4*x

    terrain =  y
    
    return terrain.reshape(1,sample)