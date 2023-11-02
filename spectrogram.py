import matplotlib.pyplot as plot
from scipy.io import wavfile
import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    args = parser.parse_args()

    sampling_frequency, signal_data = wavfile.read(args.input)

    plot.subplot(211)
    plot.title('Waveform and spectrogram view')

    plot.plot(signal_data)
    plot.xlabel('Sample')
    plot.ylabel('Amplitude')

    plot.subplot(212)
    plot.specgram(signal_data, Fs=sampling_frequency)
    plot.xlabel('Time')
    plot.ylabel('Frequency')
    plot.show()

if __name__ == "__main__":
    main()
