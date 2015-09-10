######################################################################
#
#  Written by: Marvin Fuller
#  Date: Sept 7, 2015
#  Filename: media.py
#  Purpose: the purpose of this module is to define the Movie() class
#            and it's instance variables.
#     ** Note: added the variable 'year' to display the year of the
#                movie's release.
#
######################################################################
"""The purpose of this module is to define the Movie() class
     and it's instance variables."""

#   import libraries
import webbrowser


class Movie():
    def __init__(self, movie_title, year, movie_storyline, poster_image,
                 trailer_youtube):
        """ for this class constructor which will require 5 inputs
            Movie Title, Movie Release Year, Movie storyline, a URL
            to a web based poster image, a URL for a youtube video of
            its official trailer..."""
        self.title = movie_title
        self.year = year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # define a method for playing the movie trailer from youtube URL
    def show_trailer(self):
        """  the show_trailer method will open a web browser for
               playing the movie trailer of the URL that was passed
               to this method.  """
        webbrowser.open(self.trailer_youtube_url)
