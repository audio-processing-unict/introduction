from pydub import AudioSegment
from pydub.playback import play

my_audio_file = "sine-50.wav"

sound1 = AudioSegment.from_file(my_audio_file, format="wav")

sound2 = sound1.invert_phase()
sound2.export("wav/invert-phase.wav", format="wav")

combined = sound1.overlay(sound2)
combined.export("wav/output-mix-invert-phase.wav", format="wav")

merged_audio = AudioSegment.from_wav("wav/output-mix-invert-phase.wav")
play(merged_audio)
