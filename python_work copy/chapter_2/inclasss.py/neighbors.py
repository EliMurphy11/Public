# #1. print user instructions
print("Think of an album. I will try to guess who it is by asking you questions!")
# #2 ask user for title of album
album_title = input("What is the title of the album? ")
# #3 ask user for artist of album
artist_name = input("Who is the artist of the album? ")
# #4 store album information in a dictionary
album_info = {
    'artist': artist_name,
    'album': album_title.title(),
}
# #5 print album information
print(album_info)   
print(f"You thought of the album '{album_info['album']}' by {album_info['artist']}.")   
# #6 thank user for playing
print("Thanks for playing!")
