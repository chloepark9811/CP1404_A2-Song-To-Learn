class Song:
    def __init__(self, title, artist, year, status):
        self.title = title
        self.artist = artist
        self.year = year
        self.status = status

    def mark_song(self, status):
        self.status = status
