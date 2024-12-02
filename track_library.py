from csv_manager import CSVManager
from library_item import LibraryItem

csv_manager = CSVManager("data/tracks.csv")
# library =

# library = {}
# library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
# library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
# library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)
# library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
# library["05"] = LibraryItem("Someone Like You", "Adele", 3)


def get_library():
    track_dict = {}
    rows = csv_manager.read()
    for row in rows:
        track_dict[row['track_number']] = LibraryItem(
            row['name'],
            row['artist'],
            row['artist_image'],
            int(row['rating']),
            int(row['play_count'])
        )

    return track_dict

library = get_library()

def get_all_track_numbers():
    return list(library.keys())

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
        csv_manager.write(library)
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        csv_manager.write(library)
    except KeyError:
        return

def get_artist_image(key):
    try:
        item = library[key]
        return item.artist_image
    except KeyError:
        return -1
