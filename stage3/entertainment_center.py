# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes
#instance top_story
toy_story = media.Movie('Toy Story','https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg','https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar','https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
	'https://www.youtube.com/watch?v=5PSNL1qE6VY')

age_of_ultron = media.Movie('Avengers: Age of Ultron','https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg',
	'https://www.youtube.com/watch?v=tmeOjFno6Do')

harry_potter = media.Movie('Harry Potter and the Chamber of Secrets','https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg',
	'https://www.youtube.com/watch?v=1bq0qff4iF8')

iron_man_3 = media.Movie('Iron Man 3','https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Iron_Man_3_theatrical_poster.jpg/220px-Iron_Man_3_theatrical_poster.jpg',
	'https://www.youtube.com/watch?v=aV8H7kszXqo')

three_idiots = media.Movie('3 Idiots','https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg',
	'https://www.youtube.com/watch?v=K0eDlFX9GMc')

list_of_movies = [toy_story,avatar,age_of_ultron,harry_potter,iron_man_3,three_idiots]

fresh_tomatoes.open_movies_page(list_of_movies)
