import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib


# Helper function to update the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear all existing text
    text_area.insert(1.0, content)  # Insert new content


class CreateTrackList:
    def __init__(self, window):
        # Initialize the CreateTrackList screen
        self.track_list = {}  # Dictionary to store selected tracks
        self.window = window
        self.window.geometry("750x350")  # Set the window size
        self.window.title("Create Track List")  # Set the title of the window

        # Label for track number input
        self.track_number_lbl = tk.Label(window, text="Enter A Track Number:")
        self.track_number_lbl.grid(column=0, row=0, padx=10, pady=0)

        # Entry field for track number input
        self.track_number_entry = tk.Entry(window, width=3)
        self.track_number_entry.grid(column=1, row=0, padx=10, pady=10)

        # Button to add a track to the list
        self.track_number_btn = tk.Button(window, text="Add To Track List", command=self.add_track_list)
        self.track_number_btn.grid(column=2, row=0, padx=10, pady=10)

        # ScrolledText widget to display the current track list
        self.list_txt = tkst.ScrolledText(window, width=70, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Button to reset the track list
        self.reset_btn = tk.Button(window, text="Reset", command=self.reset)
        self.reset_btn.grid(column=3, row=0, padx=0, pady=10)

        # Button to play tracks
        self.play_btn = tk.Button(window, text="Play", command=self.play)
        self.play_btn.grid(column=0, row=3, padx=0, pady=0)

        # Button to go back to the main screen
        self.back_btn = tk.Button(window, text="Back", command=self.back)
        self.back_btn.grid(column=1, row=3, padx=10, pady=10)

    # Reset the track list and clear the display
    def reset(self):
        self.list_txt.delete("1.0", tk.END)  # Clear the text area
        self.track_list = {}  # Reset the track list dictionary

    # Navigate back to the main screen
    def back(self):
        self.window.destroy()  # Close the current window
        main_root = tk.Tk()  # Create a new Tkinter root window
        fonts.configure()  # Configure fonts (if needed)
        from screens.track_player import TrackPlayer  # Import the TrackPlayer screen
        TrackPlayer(main_root)  # Initialize the main application
        main_root.mainloop()  # Start the Tkinter event loop for the new window

    # Add a track to the track list
    def add_track_list(self):
        track_number = self.track_number_entry.get()  # Get the entered track number

        # Validate the track number against the library
        track_numbers = lib.get_all_track_numbers()  # Get all valid track numbers
        if not track_number in track_numbers:
            messagebox.showerror("Error", "Track Number Is Invalid")  # Show error if invalid
            return

        # Add the track to the track list dictionary
        self.track_list[track_number] = lib.library[track_number]

        # Update the display with the updated track list
        set_text(self.list_txt, self.get_track_list())

        # Show a success message
        messagebox.showinfo("Successful", "Add Completely")

    # Generate a string representation of the current track list
    def get_track_list(self):
        output = ""
        for key in self.track_list:
            item = self.track_list[key]  # Get the track object
            output += f"{key} {item.info()} Play Count: {item.play_count}\n"  # Add track information to the output string
        return output

    # Simulate playing the tracks by incrementing their play count
    def play(self):
        for key in self.track_list:
            lib.increment_play_count(key)  # Increment the play count for each track in the list

        # Update the display with the updated track list
        set_text(self.list_txt, self.get_track_list())
