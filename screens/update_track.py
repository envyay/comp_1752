import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox

import font_manager as fonts
import track_library as lib


# Helper function to update the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear existing content
    text_area.insert(1.0, content)  # Insert new content


class UpdateTrack:
    def __init__(self, window):
        # Initialize the UpdateTrack screen
        self.track_list = {}  # Dictionary to store updated tracks
        self.window = window
        self.window.title("Update Track")  # Set window title
        self.window.geometry("600x350")  # Set window size


        # Label and entry for track number input
        self.track_number_lbl = tk.Label(window, text="Enter A Track Number:")
        self.track_number_lbl.grid(column=0, row=0, padx=10, pady=10)

        self.track_number_entry = tk.Entry(window, width=3)
        self.track_number_entry.grid(column=1, row=0, padx=0, pady=10)

        # Label and entry for new rating input
        self.new_rating_lbl = tk.Label(window, text="Enter New Rating (1-5):")
        self.new_rating_lbl.grid(column=0, row=1, padx=10, pady=10)

        self.new_rating_entry = tk.Entry(window, width=3)
        self.new_rating_entry.grid(column=1, row=1, padx=0, pady=10)

        # Button to update the track rating
        self.update_rating_btn = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_rating_btn.grid(column=0, row=4, padx=10, pady=10)

        # ScrolledText widget to display the updated track list
        self.list_txt = tkst.ScrolledText(window, width=70, height=12, wrap="none")
        self.list_txt.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Button to return to the main screen
        self.back_btn = tk.Button(window, text="Back", command=self.back)
        self.back_btn.grid(column=1, row=4, padx=10, pady=10)

    # Navigate back to the main screen
    def back(self):
        self.window.destroy()  # Close the current window
        main_root = tk.Tk()  # Create a new Tkinter root window
        fonts.configure()  # Configure fonts (if needed)
        from screens.track_player import TrackPlayer  # Import the TrackPlayer screen
        TrackPlayer(main_root)  # Initialize the main application
        main_root.mainloop()  # Start the Tkinter event loop for the new window

    # Update the rating of a track
    def update_rating(self):
        track_number = self.track_number_entry.get().strip()  # Get and trim the entered track number
        track_numbers = lib.get_all_track_numbers()  # Fetch valid track numbers

        # Check if the track number is valid
        if track_number not in track_numbers:
            messagebox.showerror("Error", "Track Number Is Invalid")
            return

        # Validate the entered rating
        rating_entry = self.new_rating_entry.get().strip()
        if not rating_entry.isdigit():  # Ensure the rating is a number
            messagebox.showerror("Error", "Invalid input. Please enter an integer in Enter New Rating (1-5):")
            return

        rating = int(rating_entry)
        if rating <= 0 or rating > 5:  # Ensure the rating is within the valid range
            messagebox.showerror("Error", "Rating must be between 1 and 5.")
            return

        # Update the rating in the library
        lib.set_rating(track_number, rating)
        self.track_list[track_number] = lib.library[track_number]  # Update local track list

        # Provide feedback to the user
        messagebox.showinfo("Success", "Rating Updated")

        # Update the displayed track list
        set_text(self.list_txt, self.get_track_list())

    # Generate a string representation of the updated track list
    def get_track_list(self):
        output = ""
        for key in self.track_list:
            item = self.track_list[key]  # Fetch the track object
            output += f"{key} {item.info()} Play Count: {item.play_count}\n"  # Append track details to output
        return output
