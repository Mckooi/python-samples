import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

pursuit_of_happyness = media.Movie("The Pursuit of Happyness",
                     "Real life of Chris Garner, an American entrepreneur, investor, stockbroker, motivational speaker, author, and philanthropist who, during the early 1980s, struggled with homelessness while raising his toddler son",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                     "https://youtu.be/89Kq8SDyvfg")

#print(pursuit_of_happyness.storyline)
#pursuit_of_happyness.show_trailer()

movies = [toy_story, avatar, pursuit_of_happyness]

print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__

fresh_tomatoes.open_movies_page(movies)
