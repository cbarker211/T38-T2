
def what_to_watch_next(description, movie_description):
    pass

#Create an empty list and add each movie description in the movies.txt file.
movie_descriptions = []
with open("movies.txt", 'r') as f:
    for count, line in enumerate(f):
        movie_descriptions.append(line.strip())

#Run the function using the supplied description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(what_to_watch_next(description, movie_descriptions))
