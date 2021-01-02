def song_decoder(song):
    song = song.split("WUB")
    fixed_song = []
    for word in song:
    	if word != '':
    		fixed_song += word
    return ''.join(fixed_song)