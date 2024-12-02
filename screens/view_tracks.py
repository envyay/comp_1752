import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk

import track_library as lib
import font_manager as fonts

# Helper function to update the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear all existing content in the text area
    text_area.insert(1.0, content)  # Insert new content starting at the beginning


class TrackViewer:
    def __init__(self, window):
        self.window = window
        # Set window dimensions and title
        window.geometry("950x350")
        window.title("View Tracks")

        self.photo = None

        # Button to display a list of all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label prompting the user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry field for the user to input a track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to view the details of a specific track
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Button to go back to the main screen
        self.back_btn = tk.Button(window, text="Back", command=self.back)
        self.back_btn.grid(column=4, row=0, padx=10, pady=10)

        # Create a label widget prompting the user to enter an artist or track name
        self.enter_artist_or_track_lbl = tk.Label(window, text="Enter Artist or Track")
        self.enter_artist_or_track_lbl.grid(row=1, column=0, padx=10, pady=10)

        # Create an entry widget where the user can input the artist or track name
        self.search_entry = tk.Entry(window, width=48)
        self.search_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create a button labeled "Search" that triggers the search functionality when clicked
        self.search_btn = tk.Button(window, text="Search", command=self.search)
        self.search_btn.grid(row=1, column=2, padx=0, pady=0)

        # ScrolledText widget to display the list of tracks
        self.list_txt = tkst.ScrolledText(window, width=64, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget to display the details of a specific track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=2, column=3, sticky="NW", padx=10, pady=10)

        # self.photo = ImageTk.PhotoImage(Image.open('image/pink_floyd.png').resize((100, 100)))
        self.artist_image_lbl = tk.Label(window)
        self.artist_image_lbl.grid(row=2, column=4, sticky="NW", padx=10, pady=10)

        # Label to display the status of the application
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically list all tracks when the application starts
        self.list_tracks_clicked()

    # Method to handle the 'View Track' button click
    def view_tracks_clicked(self):
        key = self.input_txt.get()  # Get the track number entered by the user
        name = lib.get_name(key)  # Retrieve the track name based on the input key
        if name is not None:
            # If track exists, retrieve additional details and display them
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            artist_image = lib.get_artist_image(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)  # Display the track details

            self.change_artist_image(artist_image)
        else:
            # If track doesn't exist, display an error message
            set_text(self.track_txt, f"Track {key} not found")
            self.change_artist_image('')
        self.status_lbl.configure(text="View Track button was clicked!")  # Update the status label

    # Method to handle the 'List All Tracks' button click
    def list_tracks_clicked(self):
        track_list = lib.list_all()  # Retrieve the list of all tracks
        set_text(self.list_txt, track_list)  # Display the list in the ScrolledText widget
        self.status_lbl.configure(text="List Tracks button was clicked!")  # Update the status label

    # Method to handle the 'Back' button click
    def back(self):
        self.window.destroy()  # Close the current window
        main_root = tk.Tk()  # Create a new Tkinter window
        fonts.configure()  # Apply font settings (from font_manager)
        # Import and initialize the main application screen
        from screens.track_player import TrackPlayer
        TrackPlayer(main_root)
        main_root.mainloop()  # Start the main event loop for the new window

    def change_artist_image(self, artist_image):
        # Check if the artist_image is None or an empty string
        if artist_image is None or artist_image == "":
            # Set a default "not found" image if no valid image path is provided
            artist_image = 'image/not_found.png'

        # Load the image, resize it to 100x100 pixels, and convert it for use in Tkinter
        self.photo = ImageTk.PhotoImage(Image.open(artist_image).resize((100, 100)))
        # Update the label displaying the artist image with the new photo
        self.artist_image_lbl.config(image=self.photo)

    def search(self):
        # Get the search query from the search entry widget and convert it to lowercase
        search_entry = self.search_entry.get().lower()
        output = ''  # Initialize an empty string to store the search results

        # Iterate through the library dictionary to find matches
        for key in lib.library:
            track = lib.library[key]  # Retrieve the track object
            # Check if the search query matches the artist or track name (case-insensitive)
            if search_entry in track.artist.lower() or search_entry in track.name.lower():
                # Append the matching track's key and information to the output
                output += f"{key} {track.info()}\n"

        # Update the text widget to display the search results
        set_text(self.list_txt, output)







