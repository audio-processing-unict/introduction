from scipy.io import wavfile
import numpy

mean = 0
std = 1 
num_samples = 100000
samples = numpy.random.normal(mean, std, size=num_samples)

wavfile.write("white-noise.wav", 44100, samples)
