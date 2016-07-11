# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser


class Movie():#object
    """ This class provides a way to store movie related information 
        INPUT: movie title, movie poster url, movie trailor  youtube url
        Output: construct instances of class Movie
        """
   
    def __init__(self,movie_title,poster_image,youtube_trailor):#constructor
		self.title = movie_title #instance variable
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailor 