def make_album(name, album, song=None):
    album_info = {'name': name, 'album': album}

    if song:
        album_info['song'] = song

    return album_info

# make_album(name='name1', album='album1')
# make_album(name='name2', album='album2', song='song_name')

def input_info(message):
    return ((input(message)).lower()).strip()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    # ai_name = input_info(message="Author's name: ")
    
    while True:
        ai_name = input_info(message="Author's name: ")
        if (len(ai_name)) != 0:
            break

    if ai_name == 'q':
        break
    ai_album = input_info(message="Albom's name: ")
    if ai_album == 'q':
        break
    ai_song = input_info(message="Song name: ")
    if ai_song == 'q':
        break

    print("--- Result ---")
    print(make_album(name=ai_name, album=ai_album, song=ai_song))