import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
	"""
	Represent a note in the notebook. Match againt a
	string in searchs and store tags for each note.
	"""

	def __init__(self, memo, tags=""):
		"""
		initialize a note with memo and optional
		space-separated tags. Automatically set the note's
		creation date and a unique id.
		"""
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		"""
		Determine if this note matches the filter
		text. Return True if it matches, False otherwise.

		Search iscase sensitive and matches both text and tags.
		"""
		is_match = filter in self.memo or filter in self.tags
		return is_match

class Notebook:
	"""
	Represent a collection of notes that can be tagged,
	modified, and searched.
	"""

	def __init__(self):
		"""Initialize a notebook with an empty list."""
		self.notes = []

	def new_note(self, memo, tags=""):
		"""Create a new note amd add it to the list."""
		self.notes.append(Note(memo, tags))

	def _find_note(self, note_id):
		"""Locate the note with the given id."""
		for note in self.notes:
			if str(note_id) == str(note.id):
				return note
		return None

	def modify_memo(self, note_id, memo):
		"""
		Find the note with the given id and changes its
		moeo to the given value.
		"""
		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False

	def modify_tags(self, note_id, tags):
		"""
		Find the note with the given id and change its
		tags to the given value.
		"""
		note = self._find_note(note_id)
		if note:
			note.tags = tags
			return True
		return False

	def search(self, filter):
		"""
		Find all notes that match the given filter
		string.
		"""
		match_list = [note for note in self.notes if note.match(filter)]
		return match_list
