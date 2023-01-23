class GenreValidate:
    @staticmethod
    def validator(genre):
        allowed_genres = ["Metal", "Rock", "Jazz"]

        if genre not in allowed_genres:
            raise ValueError(f"Our group doesn't play {genre}!")
        return genre
