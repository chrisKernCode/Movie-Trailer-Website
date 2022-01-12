# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes
# Movie data
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=wA_DGWIZh6U")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet", 
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")


captain_fantastic = media.Movie("Captain Fantastic",
                    "A family living in the wilderness", 
                    "https://upload.wikimedia.org/wikipedia/en/c/c2/Captain_Fantastic_poster.jpg", 
                    "https://www.youtube.com/watch?v=D1kH4OMIOMc")


man_of_the_year = media.Movie("Man of the Year",
                    "A comedian becoming US president", 
                    "https://upload.wikimedia.org/wikipedia/en/2/26/Man_of_The_Year_%282006_film%29.jpg", 
                    "https://www.youtube.com/watch?v=OUH-hK_akOI")

gladiator = media.Movie("Gladiator",
                    "A soldier becoming a gladiator and fighting the Roman Emperor.", 
                    "https://upload.wikimedia.org/wikipedia/en/f/fb/Gladiator_%282000_film_poster%29.png", 
                    "https://www.youtube.com/watch?v=0BLZbrLogTo")


troy = media.Movie("Troy",
                    "The story of Achilles and the fall of Troya", 
                    "https://upload.wikimedia.org/wikipedia/en/b/b8/Troy2004Poster.jpg", 
                    "https://www.youtube.com/watch?v=znTLzRJimeY")                    
# print(avatar.storyline)
# captain_fantastic.show_trailer()

movies = [toy_story, avatar, captain_fantastic, man_of_the_year, gladiator, troy]
fresh_tomatoes.open_movies_page(movies)

