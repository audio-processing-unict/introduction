from pydub import AudioSegment

my_audio_file = "wav/sine-300.wav"

sound1 = AudioSegment.from_file(my_audio_file, format="wav")
sound2 = AudioSegment.from_file(my_audio_file.replace('300', '305'), format="wav")

combined = sound1.overlay(sound2)
combined.export("wav/mixed-300-305.wav", format="wav")
