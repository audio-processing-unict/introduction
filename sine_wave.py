import argparse
import numpy
from scipy.io import wavfile

def generate_sine_wave(frequency, duration=1.0, amplitude=1.0, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    sampling_times = numpy.linspace(0.0, duration, num_samples, dtype=numpy.float32)
    samples = amplitude * numpy.sin(frequency * sampling_times * (2.0 * numpy.pi))
    return samples

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--frequency", type=int, required=True)
    parser.add_argument("-v", "--volume", type=float, default=1.0)
    parser.add_argument("-d", "--duration", type=float, default=1.0)
    parser.add_argument("-sr", "--sample-rate", type=int, default=44100)
    args = parser.parse_args()

    samples = generate_sine_wave(args.frequency, args.duration, args.volume, args.sample_rate)

    wavfile.write("sine.wav", args.sample_rate, samples)

if __name__ == "__main__":
    main()
