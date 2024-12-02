import csv

from library_item import LibraryItem


class CSVManager:
    def __init__(self, path):
        self.path = path

    def read(self):
        _file = open(self.path, mode='r', encoding='utf-8')
        return csv.DictReader(_file)

    def write(self, tracks):
        _file = open(self.path, mode='w', encoding='utf-8', newline='')
        fieldnames = ['track_number', 'name', 'artist', 'rating', 'play_count', 'artist_image']
        writer = csv.DictWriter(_file, fieldnames=fieldnames)
        writer.writeheader()

        for key in tracks.keys():
            item = tracks[key]
            writer.writerow({
                'track_number': key,
                'name': item.name,
                'artist': item.artist,
                'rating': item.rating,
                'play_count': item.play_count,
                'artist_image': item.artist_image,
            })

