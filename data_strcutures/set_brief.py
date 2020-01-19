# set will eliminate duplicate items in a sequence
# only hashable opjects can store in a set

song_library = [('Feel Special', 'TWICE'),
				('La Vie en Rose', 'IZ*ONE'),
			    ('What Is Love?', 'TWICE'),
			    ('Kill This Love', 'BLACKPINK'),
			    ('Vampire', 'IZ*ONE'),
			    ('Dance the Night Away', 'TWICE'),
			    ('Dalla Dalla', 'ITZY'),]

artists = set()
for song, artist in song_library:
	artists.add(artist)

# set can be used to check whether a item exist
print('TWICE' in artists)

# set can be iterated
for artist in artists:
	print(f"{artist} plays good music.")

# set is an unordered sequence
print(artists)

# set need to be converted to a list before sorting it
alphabetical = list(artists)
alphabetical.sort()
print(alphabetical)
