import abc

class MediaLoader(metaclass=abc.ABCMeta):

	# defind required attributes
	@abc.abstractproperty
	def ext(self):
		pass

	# define required methods
	@abc.abstractmethod
	def play(self):
		pass

	# any class has fulfilled all requirments will become its subclass
	# this is a class method
	@classmethod
	# is the class C a subclass of this class
	def __subclasshook__(cls, C):
		# wheter the method was called on this class directly
		if cls is MediaLoader:
			# get all attributes and methods that the class has
			attrs = set(dir(C))
			# whether required methods in the set of C
			if set(cls.__abstractmethods__) <= attrs:
				return True
		return NotImplemented

## if do not supply required attributes will raise error
#class Wav(MediaLoader):
#	pass
#x = Wav()

# define a fulfilled class
class Ogg():
	ext = '.ogg'

	def play(self):
		print("this will play an ogg file")

# whether Ogg class become subclass of MediaLoader automatically
print(issubclass(Ogg, MediaLoader))

# whether the a object of Ogg is a MediaLoader type object
o = Ogg()
print(isinstance(o, MediaLoader))
