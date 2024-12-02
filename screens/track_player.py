import tkinter as tk


from screens.create_track_list import CreateTrackList
from screens.update_track import UpdateTrack
from screens.view_tracks import TrackViewer


class TrackPlayer:
    def __init__(self, window):
        self.window = window
        # Configure the main window
        self.window.title("JukeBox")  # Set the title of the window
        self.window.geometry("800x250")  # Set the window size
        self.window.configure(bg="gray")  # Set the background color

        # Create and pack a label prompting the user to select an option
        select_lbl = tk.Label(
            window,
            text="Select an option by clicking one of the buttons below",
            bg="white",
            fg="black"
        )
        select_lbl.pack(pady=10)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(window, bg="gray")
        button_frame.pack(pady=20)

        # Button to open the "View Tracks" screen
        view_tracks_btn = tk.Button(
            button_frame,
            text="View Tracks",
            command=self.view_tracks,  # Function to handle button click
            width=20
        )
        view_tracks_btn.grid(row=0, column=0, padx=10)

        # Button to open the "Create Track List" screen
        create_track_lst_btn = tk.Button(
            button_frame,
            text="Create Track List",
            command=self.create_track_list,  # Function to handle button click
            width=20
        )
        create_track_lst_btn.grid(row=0, column=1, padx=10)

        # Button to open the "Update Tracks" screen
        update_tracks_btn = tk.Button(
            button_frame,
            text="Update Tracks",
            width=20,
            command=self.update_tracks  # Function to handle button click
        )
        update_tracks_btn.grid(row=0, column=2, padx=10)

    # Method to handle the "View Tracks" button click
    def view_tracks(self):
        self.window.destroy()  # Close the current window
        main_root = tk.Tk()  # Create a new Tkinter root window
        TrackViewer(main_root)  # Initialize the TrackViewer screen
        main_root.mainloop()  # Start the Tkinter event loop for the new window

    # Method to handle the "Create Track List" button click
    def create_track_list(self):
        self.window.destroy()  # Close the current window
        main_root = tk.Tk()  # Create a new Tkinter root window
        CreateTrackList(main_root)  # Initialize the CreateTrackList screen
        main_root.mainloop()  # Start the Tkinter event loop for the new window

    # Method to handle the "Update Tracks" button click
    def update_tracks(self):
        self.window.destroy()  # Close the current window
        main_root = tk.Tk()  # Create a new Tkinter root window
        UpdateTrack(main_root)  # Initialize the UpdateTrack screen
        main_root.mainloop()  # Start the Tkinter event loop for the new window
