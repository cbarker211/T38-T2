#Import spacy and load the model.
#Using the md model as its bigger.
import spacy
nlp = spacy.load('en_core_web_md')

#Function to output best match film.
def what_to_watch_next(description, movie_descriptions):
    #Use nlp on description and each description in the list.
    description = nlp(description)
    similarities = []
    for token in movie_descriptions:
        token = nlp(token)
        similarities.append(token.similarity(description))
    #Figure out the most similar movie and output it.
    best_match_index = similarities.index(max(similarities))
    return movie_descriptions[best_match_index][0:7]

#Create an empty list and add each movie description in the movies.txt file.
movie_descriptions = []
with open("movies.txt", 'r') as f:
    for count, line in enumerate(f):
        movie_descriptions.append(line.strip())

#Run the function using the supplied description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(f"You should watch {what_to_watch_next(description, movie_descriptions)}.")
