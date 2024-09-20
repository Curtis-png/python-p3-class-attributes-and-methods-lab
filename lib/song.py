# lib/song.py

class Song:
    count = 0  # Class attribute to keep track of the number of songs created
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to count songs by genre
    artist_count = {}  # Class attribute to count songs by artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        Song.add_song_to_count()

        # Add the genre and artist to their respective lists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

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
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count

# Example Usage
if __name__ == "__main__":
    # Creating some songs
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("God's Plan", "Drake", "Rap")
    song3 = Song("Halo", "Beyonce", "Pop")
    song4 = Song("Shape of You", "Ed Sheeran", "Pop")
    song5 = Song("Old Town Road", "Lil Nas X", "Country")

    # Accessing class attributes
    print("Total number of songs:", Song.count)  # Total number of songs
    print("Unique artists:", Song.artists)  # Unique artists
    print("Unique genres:", Song.genres)  # Unique genres
    print("Count of songs by genre:", Song.get_genre_count())  # Count of songs by genre
    print("Count of songs by artist:", Song.get_artist_count())  # Count of songs by artist
