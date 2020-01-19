first_artists = {'TWICE', 'IZ*ONE', 'BLACKPINK', 'ITZY'}
second_artists = {'Red-Velvet', 'TWICE', 'GFriend'}

"""
union() return a new set containing all elements 
that are in either of the two sets
"""
print(f"All: {first_artists.union(second_artists)}")

"""
intersection() return a new set containing all elements 
that are in both original sets
"""
print(f"Both: {first_artists.intersection(second_artists)}")

"""
symmetric_difference() return a new set containing all elements 
that are in one set of the other, but not both
"""
print(f'Just one time: {first_artists.symmetric_difference(second_artists)}')


"""
difference() returns all the elements that are in the calling set, but not
in the set passwd as an argument
"""
print(f"Only in firse: {first_artists.difference(second_artists)}")

"""
issubset() return whether all of the items in the calling set are also 
in the set passed as an argument
"""
print("First is subset of sedcond: "
	f"{first_artists.issubset(second_artists)}")

"""
issuperset() return whether the set passed as an argument are part of the
calling set
"""
print("First is superset of sedcond: "
	f"{first_artists.issuperset(second_artists)}")
