"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
# TODO: write tests to show this initialisation works
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_list = SongList()
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")
        self.sort_label = Label(text="Sort by:")
        self.title_label = Label(text="Title:")
        self.add_song_button = Button(text='Add Song')
        self.clear_button = Button(text='Clear')

