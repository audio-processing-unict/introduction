import librosa    
import soundfile as sf

y, sr = librosa.load('aeiou-espeak.wav', sr=22000)
sf.write('downsample1.wav', y, sr)

y, sr = librosa.load('aeiou-espeak.wav', sr=11000)
sf.write('downsample2.wav', y, sr)
