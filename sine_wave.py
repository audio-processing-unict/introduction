import numpy
from scipy.io import wavfile

def generate_sine_wave(frequency, duration=1.0, amplitude=1.0, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    samples = numpy.sin(amplitude * 2.0 * numpy.pi * (frequency / sample_rate) \
                        * numpy.arange(num_samples).astype(numpy.float32))
    return samples

def main():
    samples = generate_sine_wave(441000)

    wavfile.write("sine.wav", 44100, samples)

if __name__ == "__main__":
    main()
