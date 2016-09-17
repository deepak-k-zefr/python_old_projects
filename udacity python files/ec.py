import media
import fresh_tomatoes
toy_story=media.Movie("Toy story"," A story of two toys","aa","https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar=media.Movie("avatar","Visit to an alien planet","aa","aa")
#print(avatar.storyline)

#toy_story.show_trailer()
batman=media.Movie("batman","story of a bat vigilante","aa","https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiOzqrNteHOAhUlHGMKHVmmDOIQ3ywIHTAA&url=http%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DIPKZl6P89u0&usg=AFQjCNHDNyjxB0Foyb9VBa4m_kUNhG4n7A&sig2=n3rLwyevo-GuMBlzszL-FQ&bvm=bv.131286987,d.cGc")
#batman.show_trailer()   
school_of_rock=media.Movie("avatar","Visit to an alien planet","aa","aa")

#movies=[toy_story,batman,school_of_rock,avatar]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
