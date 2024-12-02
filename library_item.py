class LibraryItem:

    def __init__(self, name, artist, artist_image, rating=0, play_count=0):
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = play_count
        self.artist_image = artist_image

    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
