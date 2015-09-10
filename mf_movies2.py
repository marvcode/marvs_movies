######################################################################
#
#  Written by: Marvin Fuller
#  Date: Sept 7, 2015
#  Filename: mf_class_try04.py
#  Purpose: The purpose of this program is to create the instances
#            of each movie to be used in the final website.
#
######################################################################
""" The purpose of this program is to create the instances of each
      movie to be used in the final website."""

#   import libraries
import fresh_tomatoes
import media


# Create an instance for every movie that is included in the website
# The required arguments for the class are:
#   -movie_title - Movie Title as you want it to appear on the website
#   -year - Year of the theatrical release
#   -movie_storyline - Brief synopsis of the film
#   -poster_image - A URL that points to a web based image file of
#                    the movie poster
#   -trailer_youtube - A URL that points to the youtube trailer
#                       for each movie
#

toy_story = media.Movie(
    "Toy Story", "1995",
    "A story of a boy and his toys that come to life.",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
    "https://www.youtube.com/watch?v=vwyZH85NQC4")

braveheart = media.Movie(
    "Braveheart", "1995",
    "An epic historical medieval war drama starring Mel Gibson."
    "Gibson portrays William Wallace, a 13th-century Scottish warrior"
    "who led the Scots in the First War of Scottish Independence"
    "against King Edward I of England.",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",  # noqa
    "https://www.youtube.com/watch?v=1cnoM8EiGGU")

jaws = media.Movie(
    "Jaws", "1976",
    "An American thriller directed by Steven Spielberg and based on "
    "Peter Benchley's 1974 novel of the same name. The prototypical summer "
    "blockbuster, its release is regarded as a watershed moment in motion "
    "picture history. In the story, a giant man-eating great white shark "
    "attacks beachgoers on Amity Island, a fictional New England summer "
    "resort town, prompting the local police chief to hunt it with the help "
    "of a marine biologist and a professional shark hunter.",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg",  # noqa
    "https://youtu.be/U1fu_sA7XhE")

about_time = media.Movie(
    "About Time", "2013",
    "A British romantic comedy-drama about a young man with the "
    "special ability to time travel who tries to change his past in "
    "order to improve his future.",
    "http://ecx.images-amazon.com/images/I/814fRqJ%2BAyL._SL1500_.jpg",  # noqa
    "https://youtu.be/T7A810duHvw")

lion_king = media.Movie(
    "Lion King", "1994",
    "An American animated epic musical that takes place in a"
    "kingdom of lions in Africa, and was influenced by the biblical"
    "tales of Joseph and Moses and William Shakespeare's famous play,"
    "Hamlet.",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # noqa
    "https://youtu.be/GaJWzJfoXlE")

titanic = media.Movie(
    "Titanic", "1997",
    "An American epic romantic disaster film about a fictionalized "
    "account of the sinking of the RMS Titanic, it stars Leonardo "
    "DiCaprio and Kate Winslet as members of different social classes "
    "who fall in love aboard the ship during its ill-fated maiden voyage.",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  # noqa
    "https://youtu.be/zCy5WQ9S4c0")

forest_gump = media.Movie(
    "Forest Gump", "1994",
    "Forrest Gump is an American epic romantic-comedy-drama film "
    "based on the 1986 novel of the same name by Winston Groom. The "
    "film was directed by Robert Zemeckis and stars Tom Hanks, "
    "Robin Wright, Gary Sinise, Mykelti Williamson, and Sally Field. "
    "The story depicts several decades in the life of Forrest Gump, "
    "a slow-witted and naive, but good-hearted and athletically "
    "prodigious man from Alabama who witnesses, and in some cases "
    "influences, some of the defining events of the latter half of "
    "the 20th century in the United States; more specifically, "
    "the period between Forrest's birth in 1944 and 1982.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # noqa
    "https://youtu.be/uPIEn0M8su0")

apollo_13 = media.Movie(
    "Apollo 13", "1995",
    "An American historical docudrama that dramatizes the aborted "
    "1970 Apollo 13 lunar mission, is an adaptation of the book Lost "
    "Moon: The Perilous Voyage of Apollo 13 by astronaut Jim Lovell "
    "and Jeffrey Kluger. The film depicts astronauts Lovell, Jack "
    "Swigert and Fred Haise aboard Apollo 13 for America's third Moon "
    "landing mission. En route, an on-board explosion deprives their "
    "spacecraft of most of its oxygen supply and electric power, "
    "forcing NASA's flight controllers to abort the Moon landing, and "
    "turning the mission into a struggle to get the three men home safely.",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",  # noqa
    "https://youtu.be/nEl0NsYn1fU")

raiders = media.Movie(
    "Raiders of the Lost Ark", "1981",
    "An American action-adventure film pits Indiana Jones against "
    "a group of Nazis who are searching for the Ark of the Covenant, "
    "which Adolf Hitler believes will make his army invincible.",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg",  # noqa
    "https://youtu.be/0ZOcoxjeUYo")

saving_private_ryan = media.Movie(
    "Saving Private Ryan", "1998",
    "An American epic war drama film set during the "
    "Invasion of Normandy in World War II. The film is "
    "notable for its graphic and realistic portrayal of "
    "war, and for the intensity of its opening 27 minutes, "
    "which depict the Omaha Beach assault of June 6, 1944. "
    "It follows United States Army Rangers Captain John H. "
    "Miller (Tom Hanks) and a squad as they search for a "
    "paratrooper, Private First Class James Francis Ryan, "
    "who is the last-surviving brother of four servicemen.",
    "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",  # noqa
    "https://youtu.be/zwhP5b4tD6g")


# The following list of movies will be included in the website,
#    I placed them in chronological order.
movie_list = [jaws, raiders, forest_gump, lion_king, toy_story,
              braveheart, apollo_13, titanic, saving_private_ryan,
              about_time]

# Call the class which will create the HTML output file
fresh_tomatoes.open_movies_page(movie_list)
