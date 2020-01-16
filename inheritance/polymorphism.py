class AudioFile:

	def __init__(self, filename):

		# self.ext will make init method be polymorphism
		if not filename.endswith(self.ext):
			raise Exception('Invalid file format')
		self.filename = filename

class MP3File(AudioFile):
	ext = 'mp3'

	def play(self):
		print(f"Playing {self.filename} as mp3.")

class WavFile(AudioFile):
	ext = 'wav'

	def play(self):
		print(f"Playing {self.filename} as wav.")

class OggFile(AudioFile):
	ext = 'ogg'

	def play(self):
		print(f"Playing {self.filename} as ogg.")

ogg = OggFile("myfile.ogg")
ogg.play()

mp3 = MP3File("myfile.mp3")
mp3.play()

not_a_wav = WavFile("myfile.av")
