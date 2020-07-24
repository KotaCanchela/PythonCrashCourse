# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.

# Use None to add an optional parameter to make_album()
# that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs,
# add that value to the album’s dictionary.
# Make at least one new function call that includes the number of songs on an album.


def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary describing a music album"""
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album


album = make_album('chance', 'sunshine', 27)
print(album)

album = make_album('test', 'cloudy')
print(album)

album = make_album('anothertest', 'notcloudy')
print(album)


# User Albums: Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information,
# call make_album() with the user’s input and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary describing a music album"""
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

while True:
    print(f"\nPlease enter the album's artist and title")
    print("Enter 'quit program' to quit.")
    artist = input("Enter the artist's name: ")
    if artist == 'quit program':
        break
    title = input("Enter the title's name: ")
    if title == 'quit program':
        break
    songs = int(input("Enter the amount of songs: (0 for none)"))

    album = make_album(artist, title, songs)
    print(album)