movie_genres = ["Romance", "Comedy", "Action", "Adventure", "Fantasy", "Drama", "Horror", "Mystery", "Sci-Fi"]

print("\nMovie genres list:")
for i in range(0,len(movie_genres)):
    print(f"{movie_genres[i]}")

favorite_movie_genre = input("\nWhat is your favorite movie genre? ")

if favorite_movie_genre.lower() == "romance":
    print("\nIf you like romance movies I'd suggest you watch 'Pride & Prejudice', 'A Walk to Remember', or '20th Century Girl.")
elif favorite_movie_genre.lower() == "comedy":
    print("\nIf you like comedy movies I'd suggest you watch 'Grown Ups' or 'White Chicks'.")
elif favorite_movie_genre.lower() == "action":
    print("\nIf you like action movies I'd suggest you watch 'The Hunger Games' film series.")
elif favorite_movie_genre.lower() == "adventure":
    print("\nIf you like adventure movies I'd suggest you watch 'Jumanji'.")
elif favorite_movie_genre.lower() == "fantasy":
    print("\nIf you like fantasy movies I'd suggest you watch the 'Harry Potter' film series.")
elif favorite_movie_genre.lower() == "drama":
    print("\nIf you like dramas I'd recommend you watch 'Schindler's List'.")
elif favorite_movie_genre.lower() == "horror":
    print("\nIf you like horror movies I'd suggest you watch 'It'.")
elif favorite_movie_genre.lower() == "mystery":
    print("\nIf you like mystery movies I'd suggest you watch both of the 'Enola Holmes' movies or 'Young Sherlock Holmes'.")
elif favorite_movie_genre.lower() == "sci-fi":
    print("\nIf you like sci-fi movies I'd suggest you watch 'The Maze Runner'.")
else:
    print("\nSorry, I don't have a suggestion for that movie genre.")