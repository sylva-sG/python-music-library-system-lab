class Song:
    # --- Class Attributes (Global State) ---
    count = 0
    genres = []          # List of unique genres
    artists = []         # List of unique artists
    genre_count = {}     # Dictionary tracking totals per genre: {genre: count}
    artists_count = {}   # Dictionary tracking totals per artist: {artist: count}

    def __init__(self, name, artist, genre):
        # --- Instance Attributes ---
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # --- Automatically update global data when a song is created ---
        Song.add_song_to_count()
        Song.add_to_artists(self.artist)
        Song.add_to_genres(self.genre)
        Song.add_to_artists_count(self.artist)
        Song.add_to_genre_count(self.genre)

    # --- Class Methods ---
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
