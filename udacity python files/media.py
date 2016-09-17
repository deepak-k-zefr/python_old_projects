import webbrowser
class Movie():
    """ Movie Related Information"""
    VALID_RATINGS=['G','PG','R','PG-13']
    def __init__(self,title,storyline,poster_image,youtube) :
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
