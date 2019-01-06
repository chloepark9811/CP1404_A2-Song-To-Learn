"""
Name: Park Chae Yeon
Date: 05/01/2018
Brief Project Description:
The project records the songs you learned and the ones you didn't learn.
GitHub URL: https://github.com/chloepark9811/CP1404_A2-Song-To-Learn
"""

"""
        Complete the main program in a Kivy App subclass in main.py.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from songlist import SongList


class SongsList(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_list = SongList()

        # the status bar at the top of the right side shows the number of songs learned and still to learn
        # the status bar at the bottom of the right side shows messages about the state of the program, including updating when a song is clicked on
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")

        # To "Sort by:" label
        self.sort_label = Label(text="Sort by:")
        # To add Spinner 'Artist', 'Title', 'Year', 'Required'
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year', 'Required'))
        # To add song label
        self.add_song_label = Label(text="Add New Song...")
        # To add label and text input
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False)
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False)

        # To add buttons for adding and clearing songs
        self.add_song_button = Button(text='Add Song')
        self.clear_button = Button(text='Clear')

        # Sorting the song lists
    def songs_sort(self, *args):
        """
        The code that handle the sorts base on the click of the spinner
        """
        self.song_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def build(self):
        #  Set widgets and title and open kivy
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.song_list.load_songs()
        self.song_list.sort('Artist')
        self.building_widgets()
        self.right_widgets()
        return self.root

    def building_widgets(self):

        # Creating layout for widgets

        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_song_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.artist_label)
        self.root.ids.leftLayout.add_widget(self.artist_text_input)
        self.root.ids.leftLayout.add_widget(self.year_label)
        self.root.ids.leftLayout.add_widget(self.year_text_input)
        self.root.ids.leftLayout.add_widget(self.add_song_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)
        self.spinner.bind(text=self.songs_sort)
        self.add_song_button.bind(on_release=self.add_song_handler)
        self.clear_button.bind(on_release=self.clear_fields)

    def right_widgets(self):
        self.top_label.text = "To Learn: " + str(self.song_list.get_required_songs_count()) + ". Learned: " + str(
            self.song_list.get_learned_songs_count())

        for song in self.song_list.songs:
            if song[0].status == 'n':
                song_button = Button(text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(
                    song[0].year) + ") " "(Learned)", id=song[0].title)

                song_button.background_color = [88, 89, 0, 0.3]
            else:
                song_button = Button(
                    text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(song[0].year) + ")",
                    id=song[0].title)

                song_button.background_color = [0, 88, 88, 0.3]

            song_button.bind(on_release=self.click_handler)
            self.root.ids.rightLayout.add_widget(song_button)

    # Making the difference between to learn and learned songs
    def click_handler(self, button):

        if self.song_list.get_song(button.id).status == 'n':
            self.song_list.get_song(button.id).status = 'y'
            self.root.ids.bottomLayout.text = "You need to learn " + str(self.song_list.get_song(button.id).title)

        # if button user clicked is Required to learn change it to learned and update the status bar
        else:
            self.song_list.get_song(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You have learned " + str(self.song_list.get_song(button.id).title)

        self.songs_sort()
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def clear_fields(self, *args):
        self.title_text_input.text = ""
        self.artist_text_input.text = ""
        self.year_text_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def add_song_handler(self, *args):
        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:

                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Please enter a valid number"

                else:
                    self.song_list.add_song(self.title_text_input.text, self.artist_text_input.text,
                                            int(self.year_text_input.text))
                    self.song_list.sort(self.spinner.text)
                    self.clear_fields()
                    self.root.ids.rightLayout.clear_widgets()
                    self.right_widgets()

            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def stop(self):
        self.song_list.save_file()


if __name__ == '__main__':
    app = SongsList()
    app.run()


